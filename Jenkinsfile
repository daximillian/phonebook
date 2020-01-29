 node("linux") {
    def customImage = "" 
    environment { 
    NAME = "daximillian/phonebook"
    VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
    IMAGE = ${NAME}:${VERSION}"
    }
    stage("source") {
    git 'https://github.com/daximillian/phonebook'
    }
    stage("build docker") {
    customImage = docker.build(${IMAGE})
    }
    stage("verify image") {
    sh '''
        docker run --rm -d -p 80:8080/tcp {$IMAGE}
        curl -s 'http://localhost'
    ''' 
    }
    stage("push to DockerHub") {
    withDockerRegistry(credentialsId: 'dockerhub.daximillian') {
    customImage.push()
    }
    }
    stage("deploy to EKS") {
    sh '''
        export KUBECONFIG=/home/ubuntu/kubeconfig_opsSchool-eks
        kubectl apply -f deployment.yml
        kubectl set image deployment/phonebook phonebook={$IMAGE} --record
        kubectl apply -f service.yml
        kubectl apply -f loadbalancer.yml
    '''
    }
}


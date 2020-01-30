 node("linux") {
    def customImage = "" 
    environment { 
    NAME = "daximillian/phonebook"
    VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
    IMAGE = "${NAME}:${VERSION}"
    }
    stage("source") {
    git 'https://github.com/daximillian/phonebook'
    }
    stage("build docker") {
    customImage = docker.build("daximillian/phonebook")
    }
    stage("verify image") {
    sh '''
        docker run --rm -d -p 8000:8080/tcp --name phonebook daximillian/phonebook
        sleep 20s
        curl_response=$(curl -s -o /dev/null -w "%{http_code}" 'http://localhost:8000')
        if [ $curl_response -eq 200 ]
        then
            exit 0
        else
            exit 1
        fi
    ''' 
    }
    stage("cleanup image") {
    sh '''
        docker stop phonebook
    '''
    }
    stage("push to DockerHub") {
        echo "Push to Dockerhub"
    withDockerRegistry(credentialsId: 'dockerhub.daximillian') {
    customImage.push("${env.BUILD_NUMBER}")
    customImage.push("latest")
    }
    }
    stage("deploy to EKS") {
    sh '''
        export KUBECONFIG=/home/ubuntu/kubeconfig_opsSchool-eks
        kubectl apply -f deployment.yml
        kubectl set image deployment/phonebook phonebook=${IMAGE} --record
        kubectl apply -f service.yml
        kubectl apply -f loadbalancer.yml
    '''
    }
}


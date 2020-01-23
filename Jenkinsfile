 node("linux") {
    def customImage = "" 
    stage("source") {
    git 'https://github.com/daximillian/phonebook'
    }
    stage("build docker") {
    customImage = docker.build("daximillian/phonebook")
    }
    stage("verify image") {
    sh "docker images" 
    }
    stage("push to DockerHub") {
    withDockerRegistry(credentialsId: 'dockerhub.daximillian') {
    customImage.push()
    }
    }
}



pipeline {
  agent none
  environment{
    DOCKER_TAG = getDockerTag()
  }
  stages {
    stage('Checkout Source') {
        agent any
        steps {
            git url:'https://github.com/alexnguyenit/mobile-service.git', branch:'master'
        }
    }
    stage("Build image") {
        agent any
        steps {
            script {
                myapp = docker.build("hoangnguyenngoctb/mobileservice:${DOCKER_TAG}")
            }
        }
    }
    stage("Push image") {
        agent any
        steps {
            script {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                        myapp.push("latest")
                        myapp.push("${DOCKER_TAG}")
                }
            }
        }
    }
    stage('Deploy App') {
        agent any
//         agent { label 'kubepod' }
        steps {
            sh "chmod +x changeTag.sh"
	        sh "./changeTag.sh ${DOCKER_TAG}"
            script {
//                 kubernetesDeploy(configs: "kubefile.yml", kubeconfigId: "mykubeconfig")
                withKubeConfig([credentialsId: 'KubeSecret', serverUrl: 'https://183.91.11.119:6443']) {
                    sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'
                    sh 'chmod u+x ./kubectl'
                    sh './kubectl get pods'
                    sh './kubectl apply -f kubefile-done.yml'
                }
            }
        }
    }
  }
}

def getDockerTag(){
    def tag  = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
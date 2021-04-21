pipeline {
  agent any
  stages {
    stage('Checkout Source') {
        steps {
            git url:'https://github.com/alexnguyenit/mobile-service.git', branch:'master'
        }
    }
    stage("Build image") {
        steps {
            script {
                myapp = docker.build("hoangnguyenngoctb/mobileservice:${env.BUILD_ID}")
            }
        }
    }
    stage("Push image") {
        steps {
            script {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                        myapp.push("latest")
                        myapp.push("${env.BUILD_ID}")
                }
            }
        }
    }
    stage('Deploy App') {
        steps {
            script {
//                 kubernetesDeploy(configs: "kubefile.yml", kubeconfigId: "mykubeconfig")
                withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: 'https://183.91.11.119:6443']) {
                  sh 'kubectl apply -f kubefile.yml'
                }
            }

        }
    }
  }
}
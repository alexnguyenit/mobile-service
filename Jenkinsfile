def GIT_TAG
pipeline {
  agent any
  stages {
    stage('Checkout Source') {
        steps {
            git url:'https://github.com/alexnguyenit/mobile-service.git', branch:'master'
            script {
                GIT_TAG = sh script: 'git rev-parse HEAD', returnStdout: true
                GIT_TAG = GIT_TAG.substring(0, 12)
            }
        }
    }
    stage("Build image") {
        steps {
            script {
                myapp = docker.build("hoangnguyenngoctb/mobileservice:${GIT_TAG}")
            }
        }
    }
    stage("Push image") {
        steps {
            script {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                        myapp.push("latest")
                        myapp.push("${GIT_TAG}")
                }
            }
        }
    }
    stage('Deploy App') {
//         agent { label 'kubepod' }
        steps {
            script {
                sh "chmod +x changeTag.sh"
                sh "./changeTag.sh ${GIT_TAG}"
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


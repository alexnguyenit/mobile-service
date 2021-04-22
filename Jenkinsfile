pipeline {
  agent none
  stages {
    stage('Checkout Source') {
        agent any
        steps {
            git url:'https://github.com/alexnguyenit/mobile-service.git', branch:'master'
        }
    }
//     stage("Build image") {
//         agent any
//         steps {
//             script {
//                 myapp = docker.build("hoangnguyenngoctb/mobileservice:${env.BUILD_ID}")
//             }
//         }
//     }
//     stage("Push image") {
//         agent any
//         steps {
//             script {
//                 docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
//                         myapp.push("latest")
//                         myapp.push("${env.BUILD_ID}")
//                 }
//             }
//         }
//     }
    stage('Deploy App') {
        agent any
//         agent { label 'kubepod' }
        steps {
            script {
//                 kubernetesDeploy(configs: "kubefile.yml", kubeconfigId: "mykubeconfig")
                withKubeConfig([credentialsId: 'KubeSecret', serverUrl: 'https://183.91.11.119:6443']) {
                  sh 'kubectl apply -f kubefile.yml'
                }
            }

        }
    }
  }
}
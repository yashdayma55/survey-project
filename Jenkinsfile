pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE_NAME = 'yashdayma55/survey-app'
        DOCKER_IMAGE_TAG = 'latest'
        KUBECONFIG = 'C:\\ProgramData\\Jenkins\\.kube\\config'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/yashdayma55/survey-project.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", "--no-cache .")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/pvc.yml --validate=false'
                bat 'kubectl apply -f k8s/deployment.yml --validate=false'
                bat 'kubectl apply -f k8s/service.yml --validate=false'
                bat 'kubectl apply -f k8s/ingress.yml --validate=false'
            }
        }
    }
    post {
        always {
            bat 'docker rmi %DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG% || exit 0'
        }
    }
}

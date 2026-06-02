pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "flask-cicd-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Git checkout works!'
                sh 'ls -la'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }
        
        stage('Trivy Scan') {
            steps {
                echo 'Scanning image for vulnerabilities...'
                sh "trivy image --exit-code 0 --severity HIGH,CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
        
        stage('Test Container') {
            steps {
                echo 'Running container to test...'
                sh "docker run -d -p 5001:5000 --name test-container ${IMAGE_NAME}:${IMAGE_TAG}"
                sh 'sleep 5'
                sh 'curl -f http://localhost:5001 || exit 1'
                sh 'docker stop test-container'
                sh 'docker rm test-container'
            }
        }
    }
    
    post {
        always {
            sh 'docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true'
            sh 'docker rmi ${IMAGE_NAME}:latest || true'
        }
    }
}

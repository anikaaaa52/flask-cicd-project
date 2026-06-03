pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "anikaaa/flask-cicd"
        IMAGE_TAG = "latest"
    }
    
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/anikaaaa52/flask-cicd-project.git'
            }
        }
        
        stage('Trivy FS Scan') {
            steps {
                sh 'trivy fs --exit-code 0 --severity HIGH,CRITICAL .'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }
        
        stage('Trivy Image Scan') {
            steps {
                sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL $IMAGE_NAME:$IMAGE_TAG'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                        docker logout
                    '''
                }
            }
        }
        
        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d --name flask-app -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker image prune -f'
        }
    }
}

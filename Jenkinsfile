pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-cicd-app"
    }

    stages {

        


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d --name flask-app -p 5000:5000 $IMAGE_NAME
                '''
            }
        }
    }
}

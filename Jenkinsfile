pipeline {

    agent any

    environment {
        IMAGE_NAME = "siri987/linear-regression-mlops"
        IMAGE_TAG  = "latest"
        CONTAINER_NAME = "linear-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker login -u YOUR_DOCKER_USERNAME -p YOUR_DOCKER_PASSWORD
                docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true

                docker run -d \
                    --name $CONTAINER_NAME \
                    -p 5000:5000 \
                    $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

    }
}

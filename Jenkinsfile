pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t linear-regression-app:v1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f linear-app || true
                docker run -d -p 5000:5000 --name linear-app linear-regression-app:v1
                '''
            }
        }
    }
}

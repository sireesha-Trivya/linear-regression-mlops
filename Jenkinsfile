pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python --version
                pip install -r requirements.txt
                '''
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
    }
}

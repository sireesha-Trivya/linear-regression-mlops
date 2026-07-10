pipeline {
    agent any

    environment {
        IMAGE_NAME = "siri987/linear-regression-mlops"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Verify Tools') {
            steps {
                sh '''
                    echo "===== Checking Installed Tools ====="
                    python3 --version
                    pip3 --version
                    docker --version
                    git --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    . venv/bin/activate
                    python train.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('DockerHub Login & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {

                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker stop linear-app || true
                    docker rm linear-app || true

                    docker run -d \
                        --name linear-app \
                        -p 5000:5000 \
                        ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo '====================================='
            echo 'Pipeline executed successfully!'
            echo 'Application deployed successfully!'
            echo '====================================='
        }

        failure {
            echo '====================================='
            echo 'Pipeline execution failed.'
            echo 'Check Console Output for errors.'
            echo '====================================='
        }

        always {
            cleanWs()
        }
    }
}

pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')  // Poll every 5 minutes (adjust as needed)
    }
    stages {

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
pipeline {
    agent any
    
    options {
        skipDefaultCheckout(false)
    }

    stages {
        
        stage('Cleanup') {
            steps {
                deleteDir()   // ✅ correct place
            }
        }
        stage('Debug') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Build') {
            steps {
                sh 'docker compose build'
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
                sh 'docker compose up -d'
            }
        }
    }
}

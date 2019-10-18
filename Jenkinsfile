pipeline {
    agent {
        docker {
            image 'python:3-alpine'
            args '-p 3001:3001'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'rm /var/lib/mongodb/mongod.lock'
                sh 'mongod --repair'
                sh 'service mongodb start'
                sh 'service mongodb status'
                sh 'pytest'
            }
        }
        stage('Deliver') {
            steps {
                sh 'echo App \'Delivered\'. '
            }
        }
    }
}

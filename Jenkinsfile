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
                sh 'sudo rm /var/lib/mongodb/mongod.lock'
                sh 'sudo mongod --repair'
                sh 'sudo service mongodb start'
                sh 'sudo service mongodb status'
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

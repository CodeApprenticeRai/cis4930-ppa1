pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts-alpine'
            args '-p 3001:3001'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'apk update'
                sh 'apk add mongodb'
                sh 'apk add python3'
                sh 'pip3 install --no-cache-dir -r requirements.txt'
                sh 'apk add openrc'
                sh 'mkdir /data/'
                sh 'mkdir /data/db/'
                sh 'mongod --fork --logpath /var/log/mongodb.log'
            }
        }
        stage('Test') {
            steps {
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

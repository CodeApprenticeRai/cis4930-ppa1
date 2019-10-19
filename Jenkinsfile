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
                sh 'echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories'
                sh 'apk update'
                sh 'apk add --no-cache mongodb'
                sh 'pip install --no-cache-dir -r requirements.txt'
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

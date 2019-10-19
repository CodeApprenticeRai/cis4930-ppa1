pipeline {
    agent {
        docker {
            image 'nikolaik/python-nodejs:python3.6-nodejs12-alpine'
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
                sh 'apk add mongodb'
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

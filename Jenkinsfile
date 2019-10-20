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
        stage('Build Python App') {
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
        stage('Test Python App') {
            steps {
                sh 'pytest'
            }
        }
        stage('Build Web Server'){
          steps {
            sh 'apk add npm'
            sh 'npm install -g npm@5.7.1'
            sh 'npm install'
            sh 'npm start'
          }
        }
        stage('Test Web server') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deliver') {
            steps {
                sh 'echo PPA Application Delivered. 4 / 4 Phases Complete. '
            }
        }
    }
}

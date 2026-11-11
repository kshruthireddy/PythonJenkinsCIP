pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Compilation') {
            steps {
                bat 'py -3 -m py_compile app.py test_app.py'
            }
        }

        stage('Testing') {
            steps {
                bat 'py -3 -m unittest -v'
            }
        }

        stage('Packaging') {
            steps {
                bat 'powershell -NoProfile -Command "Compress-Archive -Path app.py -DestinationPath python-app.zip -Force"'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'python-app.zip'
        }
    }
}
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Running Build Stage..."
                sh 'echo Building the project'
            }
        }

        stage('Test') {
            steps {
                echo "Running Test Stage..."
                sh 'echo Executing tests'
            }
        }

        stage('Deploy') {
            steps {
                echo "Running Deploy Stage..."
                sh 'echo Deploying application'
            }
        }

    }
}

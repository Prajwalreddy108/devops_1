pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code"
            }
        }

        stage('Build') {
            steps {
                echo "Build stage running..."
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 demo.py'
            }
        }
    }
}

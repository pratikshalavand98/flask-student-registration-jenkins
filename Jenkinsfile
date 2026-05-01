pipeline {
    agent any

    environment {
        APP_PORT = "5000"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/pratikshalavand98/flask-student-registration-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                sh 'nohup python app.py &'
            }
        }
    }

    post {
        success {
            echo "Application deployed successfully 🚀"
        }
        failure {
            echo "Build failed ❌"
        }
    }
}
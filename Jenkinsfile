pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Clone Repo') {
            steps {
                git branch: 'master',
                url: 'https://github.com/pratikshalavand98/flask-student-registration-jenkins.git'
            }
        }

        stage('Install Python Packages') {
            steps {
                powershell 'pip install -r requirements.txt'
            }
        }

        stage('Check Python') {
            steps {
                powershell 'python --version'
            }
        }

        stage('Build Success') {
            steps {
                echo "Flask App Build Successful 🎉"
            }
        }
    }
}

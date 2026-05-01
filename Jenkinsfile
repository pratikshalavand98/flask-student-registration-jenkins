pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/pratikshalavand98/flask-student-registration-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Windows\\System32\\cmd.exe" /c pip install -r requirements.txt'
            }
        }

        stage('Python Syntax Check') {
            steps {
                bat '"C:\\Windows\\System32\\cmd.exe" /c python --version'
            }
        }

        stage('Run Flask App') {
            steps {
                bat '"C:\\Windows\\System32\\cmd.exe" /c python app.py'
            }
        }
    }

    post {
        success {
            echo 'Build Successful ✅'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'master',
                url: 'https://github.com/pratikshalavand98/flask-student-registration-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Python Syntax Check') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'Flask Student Registration Build Successful 🎉'
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

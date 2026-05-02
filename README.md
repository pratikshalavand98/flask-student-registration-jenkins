# 🎓 Flask Student Registration Web Application (Jenkins CI/CD)

## 📌 Project Overview

This project is a web-based Student Registration System developed using Flask.
It allows users to register student details through a web form and stores the data securely in a MySQL database.

The application is integrated with Jenkins to automate the build and deployment process, ensuring continuous integration.

---

## 🚀 Features

* Student Registration Form
* Server-side and client-side validation
* Data stored in MySQL database
* View all registered students in tabular format
* Flash messages for success/failure
* Jenkins CI/CD pipeline integration

---

## 🛠️ Technology Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** MySQL
* **Version Control:** Git & GitHub
* **CI/CD Tool:** Jenkins
* **Deployment (Optional):** AWS EC2

---

## 📁 Project Structure

```
flask-student-registration-jenkins/
│── app.py
│── requirements.txt
│── Jenkinsfile
│── README.md
│
├── templates/
│   ├── register.html
│   ├── students.html
│
├── static/
│   └── style.css (optional)
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/<your-username>/flask-student-registration-jenkins
cd flask-student-registration-jenkins
```

### 🔹 2. Install Dependencies

```
pip install -r requirements.txt
```

### 🔹 3. Setup MySQL Database

Login to MySQL and run:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    course VARCHAR(50),
    address TEXT
);
```

---

### 🔹 4. Configure Database Connection

Update database credentials inside your Flask app:

```
host="localhost"
user="root"
password="yourpassword"
database="student_db"
```

---

### 🔹 5. Run Application

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🔄 Jenkins CI/CD Pipeline

This project uses Jenkins to automate build and deployment.

### 📌 Pipeline Stages:

1. Clone GitHub Repository
2. Install Dependencies
3. Run Flask Application

### 📌 Sample Jenkinsfile:

```groovy
pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/<your-username>/flask-student-registration-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}
```

---

## 📸 Screenshots

(Add screenshots here)

* Registration Form
* Student List Page
* Jenkins Pipeline Success

---

## 🌐 Deployment (Optional)

The application can be deployed on AWS EC2 instance by installing Python, MySQL, and Jenkins.

---

## 🧠 How It Works

1. User fills the registration form
2. Flask processes the request
3. Data is stored in MySQL database
4. User is redirected to the students page
5. All records are displayed in table format

---

## 🔗 GitHub Repository

Add your repository link here:

```
https://github.com/<your-username>/flask-student-registration-jenkins
```

---

## 🎯 Future Enhancements

* Edit/Delete student records
* Search functionality
* User authentication system
* Docker containerization
* Deployment with Nginx & Gunicorn

---

## 👨‍💻 Author
**Pratiksha Lavand**  
☁️ Aspiring Cloud & DevOps Engineer  
🔗 GitHub: [github.com/your-username](https://github.com/pratikshalavand98/)  
🔗 LinkedIn: [linkedin.com/in/your-linkedin-id](https://www.linkedin.com/in/pratiksha-lavand/)

---

## 📜 License

This project is for educational purposes.

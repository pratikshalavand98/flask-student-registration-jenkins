from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

cursor = db.cursor()


# ---------------- HOME PAGE ----------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- REGISTER STUDENT ----------------
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    cursor.execute("""
        INSERT INTO students (name, email, phone, course, address)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, phone, course, address))

    db.commit()

    return redirect('/students')


# ---------------- VIEW STUDENTS ----------------
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('view.html', students=data)


# ---------------- EDIT STUDENT ----------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        cursor.execute("""
            UPDATE students 
            SET name=%s, email=%s, phone=%s, course=%s, address=%s
            WHERE id=%s
        """, (name, email, phone, course, address, id))

        db.commit()
        return redirect('/students')

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()

    return render_template("edit.html", student=student)


# ---------------- DELETE STUDENT ----------------
@app.route('/delete/<int:id>')
def delete(id):

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()

    return redirect('/students')


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
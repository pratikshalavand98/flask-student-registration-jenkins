from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'student_db'
}

# Home (Form Page)
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            course = request.form['course']
            address = request.form['address']
            contact = request.form['contact']

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = """
            INSERT INTO students (name, email, phone, course, address, contact)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(query, (name, email, phone, course, address, contact))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('students'))

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('register.html')


# View Students Page
@app.route('/students')
def students():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('students.html', students=data)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
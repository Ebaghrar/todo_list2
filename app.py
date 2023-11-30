from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurer la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todolist'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task_content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (content) VALUES (%s)", (task_content,))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template,request,redirect
import pyodbc,runpy
app = Flask(__name__)

password = 'cal'
conn_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Lenovo\Desktop\Coding\Flask\pjk1\Lab.accdb;PWD='+ password
conn = pyodbc.connect(conn_string)
#runpy.run_path("dbcon.py")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/regis")
def regis():
    return render_template('Register.html')

@app.route("/user")
def user():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM userTable")
        rows = cur.fetchall()
    return render_template('user.html',data = rows)


if __name__ == "__main__":
    app.run(debug=True)



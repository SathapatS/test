from flask import Flask,render_template,request,redirect
import dbcon
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/regis")
def regis():
    return render_template('Register.html')

@app.route("/user")
def user():
    with dbcon.conn:
        cur = dbcon.conn.cursor()
        cur.execute("SELECT * FROM userTable")
        rows = cur.fetchall()
    return render_template('user.html',data = rows)


if __name__ == "__main__":
    app.run(debug=True)






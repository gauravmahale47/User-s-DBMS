import pymysql
from flask import *

db = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="hirect")

app = Flask(__name__)

cursor = db.cursor()

@app.route("/")
def list():
    allq = "SELECT * FROM users"
    cursor.execute(allq)
    data = cursor.fetchall()
    return render_template("list.html", users=data)

@app.route("/create", methods=["POST"])
def create():
    uname = request.form.get("uname")
    email = request.form.get("email")
    monumber = request.form.get("monumber")
    try:
        insq = "INSERT INTO users VALUES(NULL, '{}','{}','{}')".format(uname,email,monumber)
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('list'))    
    except:
        db.rollback()
        return "<h1>Student addition failed!!!</h1>"

@app.route("/edit/<id>")
def edit(id):
    allq = "SELECT * FROM users"
    cursor.execute(allq)
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM users WHERE id = {}".format(id))
    datasingle = cursor.fetchall()
    return render_template("edit.html",users=data, user=datasingle)

@app.route("/update", methods=['POST'])
def update():
    uname = request.form.get("uname")
    email = request.form.get("email")
    monumber = request.form.get("monumber")
    uid  =  request.form.get("uid")
    try:
        upq = "UPDATE users SET name='{}', email='{}', mobile_no='{}' WHERE id = {}".format(uname,email,monumber,uid)
        cursor.execute(upq)
        db.commit()
        return redirect(url_for('list'))
    except:
        db.rollback()
        return "<h1>Student information updation failed!!!</h1>"

@app.route("/delete/<id>")
def delete(id):
    try:
        delq = "DELETE FROM users WHERE id = {}".format(id)
        cursor.execute(delq)
        db.commit()
        return redirect(url_for('list'))
    except:
        db.rollback()
        return "<h1>User deletion failed!!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)



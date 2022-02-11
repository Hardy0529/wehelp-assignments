
from flask import Flask, redirect, template_rendered, url_for, render_template, request, session
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="12345678",
    database="website")

mycursor = mydb.cursor()


app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/signup", methods=["POST"])
def register():
    registerName = request.form["username"]
    registerAccount = request.form["account"]
    registerPassword = request.form["password"]

    mycursor.execute(
        "SELECT `name` FROM `member`  WHERE `username` = '" + registerAccount + "';")

    data = mycursor.fetchone()
    if not data == None:
        return redirect(url_for("erro", message="帳號已經被註冊"))
    else:
        if registerName == "" or registerAccount == "" or registerPassword == "":
            return redirect(url_for("erro", message="帳號、密碼不得為空值"))
        else:
            mycursor.execute(
                "INSERT INTO `member`(`name`,`username`,`password`) VALUES('"+registerName+"','"+registerAccount+"','"+registerPassword+"')")
            mydb.commit()

    return redirect(url_for("home"))


@ app.route("/signin", methods=["POST"])
def login():

    loginAccount = request.form["account"]
    loginPassword = request.form["password"]

    if loginAccount == "" or loginPassword == "":
        return redirect(url_for("erro", message="請輸入帳號、密碼"))
    else:
        mycursor.execute(
            "SELECT `username` FROM `member`  WHERE `username` = '" + loginAccount + "';")
        account = mycursor.fetchone()

        mycursor.execute(
            "SELECT `password` FROM `member`  WHERE `username` = '" + loginAccount + "';")
        password = mycursor.fetchone()

        mycursor.execute(
            "SELECT `name` FROM `member`  WHERE `username` = '" + loginAccount + "';")
        username = mycursor.fetchone()

        if account == None:
            return redirect(url_for("erro", message="帳號、或密碼輸入錯誤"))
        else:
            account = account[0]
            password = password[0]
            username = username[0]
            if loginAccount == account and loginPassword == password:
                account = loginAccount
                session["account"] = account

                password = loginPassword
                session["password"] = password

                session["username"] = username

                return redirect(url_for("user"))

            elif loginAccount != account or loginPassword != password:
                return redirect(url_for("erro", message="帳號、或密碼輸入錯誤"))


@ app.route("/member/")
def user():

    if "account" in session:
        if "password" in session:
            username = session["username"]
            return render_template("member.html", member=username)
    else:
        return redirect(url_for("home"))


@ app.route("/signout")
def logout():

    session.pop("account", None)
    return redirect(url_for("home"))


@ app.route("/erro/")
def erro():
    message = request.args.get("message", "")
    return render_template("erro.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

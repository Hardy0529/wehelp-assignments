from flask import Flask, redirect, url_for, render_template, request, session, jsonify
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

    selectSql = "SELECT `name` FROM `member`  WHERE `username` = %s"
    adr = (registerAccount,)
    mycursor.execute(selectSql, adr)
    data = mycursor.fetchone()

    if not data == None:
        return redirect(url_for("erro", message="帳號已經被註冊"))
    else:
        if registerName == "" or registerAccount == "" or registerPassword == "":
            return redirect(url_for("erro", message="帳號、密碼不得為空值"))
        else:
            sql = "INSERT INTO `member`(`name`,`username`,`password`) VALUES(%s,%s,%s)"
            val = (registerName, registerAccount, registerPassword)
            mycursor.execute(sql, val)
            mydb.commit()

    return redirect(url_for("home"))


@app.route("/signin", methods=["POST"])
def login():
    loginAccount = request.form["account"]
    loginPassword = request.form["password"]

    if loginAccount == "" or loginPassword == "":
        return redirect(url_for("erro", message="請輸入帳號、密碼"))
    else:
        selectSql = "SELECT `name`,`username`,`password` FROM `member`  WHERE `username` = %s;"
        adr = (loginAccount,)
        mycursor.execute(selectSql, adr)
        accountQuery = mycursor.fetchone()

        if accountQuery == None:
            return redirect(url_for("erro", message="帳號、或密碼輸入錯誤"))
        else:
            username = accountQuery[0]
            account = accountQuery[1]
            password = accountQuery[2]

            if loginAccount == account and loginPassword == password:
                session["account"] = loginAccount
                session["password"] = loginPassword
                session["username"] = username
                return redirect(url_for("user"))

            elif loginAccount != account or loginPassword != password:
                return redirect(url_for("erro", message="帳號、或密碼輸入錯誤"))


@app.route("/member/")
def user():
    if "account" in session:
        if "password" in session:
            username = session["username"]
            return render_template("member.html", member=username)
    else:
        return redirect(url_for("home"))


@app.route("/api/members", methods=["GET", "POST"])
def get_stores():
    if request.method == "GET":
        registerAccount = request.args.get("username")

        selectSqla = "SELECT `id`,`name`,`username` FROM `member`  WHERE `username` = %s "
        adra = (registerAccount,)
        mycursor.execute(selectSqla, adra)
        data = mycursor.fetchone()

        if data == None:
            return jsonify({"data": None})
        else:
            member = {
                "id": data[0],
                "name": data[1],
                "username": data[2]
            }
            return jsonify({"data": member})


@app.route("/signout")
def logout():
    session.pop("account", None)
    return redirect(url_for("home"))


@app.route("/erro/")
def erro():
    message = request.args.get("message", "")
    return render_template("erro.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=3000)

from flask import Flask, redirect, url_for, render_template, request, session


app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/signin", methods=["POST"])
def login():

    account = "test"
    password = "test"
    if request.form["account"] == "" or request.form["password"] == "":
        return redirect(url_for("erro", message="請輸入帳號、密碼"))

    elif request.form["account"] != account or request.form["password"] != account:
        return redirect(url_for("erro", message="帳號、或密碼輸入錯誤"))

    account = request.form["account"]
    session["account"] = account

    password = request.form["password"]
    session["password"] = password

    return redirect(url_for("user"))


@app.route("/member/")
def user():
    if "account" in session:
        if "password" in session:
            return render_template("member.html")
    else:
        return redirect(url_for("home"))


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

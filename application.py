from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

db = SQL("sqlite:///amiblog.db")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")


        if not username or password or confirm:
            return render_template("register.html")

        user = db.execute("SELECT * FROM usuarios WHERE username = :username", username = username)

        if len(user) == 1:
            return render_template("register.html")

        if len(user) != 1 and password == confirm:
           x = db.execute(f"INSERT INTO usuarios (username, password, nombre, apellido) VALUES (:username,:password,:nombre, :apellido)", username = request.form.get("username"), password = generate_password_hash(request.form.get("password"), nombre = name, apellido = lastname))

    return render_template("register.html")



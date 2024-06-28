import json
import os
from functools import wraps

from flask import flash, g, redirect, render_template, request, session, url_for

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Smart condominium | Home")


@app.route("/contato")
def contato():
    return render_template("contato.html", titulo="Ajuda")


@app.route("/cuidados")
def cuidados():
    return render_template("cuidados.html", titulo="Cuidados")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", titulo="Sobre")


@app.route("/inscrever")
def inscrever():
    return render_template("inscrever.html", titulo="inscrever")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/erro")
def erro():
    return render_template("erro.html")


if __name__ == "__main__":
    app.run(debug=True)

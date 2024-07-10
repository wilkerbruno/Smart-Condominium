from flask import redirect, render_template, request, session, url_for

from condominio import app, db, path


@app.route("/")
def index():
    return render_template("index.html", titulo="Smart condominium | Home")


@app.route("/cadastro_funcionario")
def cadastro_funcionario():
    return render_template("cadastro_funcionario.html", titulo="Cadastro de Funcionario")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", titulo="Sobre")


@app.route("/cadastro_morador")
def cadastro_morador():
    return render_template("cadastro_morador.html", titulo="Cadastro de Morador")


@app.route("/cadastro_unit")
def cadastro_unit():
    return render_template("cadastro_unit.html", titulo="cadastro de Unidades")


@app.route("/cobranca")
def cobranca():
    return render_template("cobranca.html", titulo="Cobranças")


@app.route("/fazer_reservas")
def fazer_reservas():
    return render_template("fazer_reservas.html", titulo="Fazer Reservas")


@app.route("/funcionarios")
def funcionarios():
    return render_template("funcionarios.html", titulo="Funcionarios")


@app.route("/reservas")
def reservas():
    return render_template("reservas.html", titulo="Reservas")


@app.route("/resultados")
def resultados():
    return render_template("resultados.html", titulo="Resultados")


@app.route("/units")
def units():
    return render_template("units.html", titulo="units")


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

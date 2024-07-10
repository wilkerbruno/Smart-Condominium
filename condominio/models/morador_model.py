from condominio import db


class Morador(db.Model):
    __tablename__ = 'morador'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, sobrenome, cpf, celular, telefone, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.celular = celular
        self.telefone = telefone
        self.email = email

    def __repr__(self):
        return '<Morador'

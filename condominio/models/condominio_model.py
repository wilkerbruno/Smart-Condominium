from condominio import db


class Condominio(db.Model):
    __tablename__ = 'condominio'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(35), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True, nullable=False)
    nome_sindico = db.Column(db.String(50), nullable=False)
    telefone_sindico = db.Column(db.Integer, nullable=False)
    email_sindico = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, nome, cep, estado, cidade, endereco, numero, celular, telefone, email, nome_sindico,
                 telefone_sindico, email_sindico):
        self.nome = nome
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.endereco = endereco
        self.numero = numero
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.nome_sindico = nome_sindico
        self.telefone_sindico = telefone_sindico
        self.email_sindico = email_sindico

    def __repr__(self):
        return f'<Condominio'

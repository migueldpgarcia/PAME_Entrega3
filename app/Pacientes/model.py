from sqlalchemy.orm import backref
from app.extensions import db
from app.association import association_table

class Paciente (db.Model):
    __tablename__ = "paciente"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)

    consultas = db.relationship ('Consulta', backref = 'paciente')
    exames = db.relationship ('Exame', backref = 'paciente')
    receitas = db.relationship ('Receita', backref = 'paciente')

    medicos = db.relationship ('Medico', secondary=association_table, backref='paciente')
    
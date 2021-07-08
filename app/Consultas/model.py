from app.extensions import db

class Consulta (db.Model):
    __tablename__ = "consulta"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    
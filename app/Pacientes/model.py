from app.extensions import db

class Paciente (db.Model):
    __tablename__ = "paciente"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    
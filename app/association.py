from app.extensions import db

association_table = db.Table("association", db.Model.metadata,
                    db.Column ("medicos", db.Integer, db.ForeignKey("medico.id")),
                    db.Column ('pacientes', db.Integer, db.ForeignKey("paciente.id")))
from config import db

class Disciplina(db.Model):
    __tablename__ = "disciplinas"  
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    id_disciplina = db.Column(db.Integer, unique=True, nullable=False)
    publica = db.Column(db.Boolean, default=True, nullable=False)

class ProfessorDisciplina(db.Model):
    __tablename__ = "professor_disciplina"
    
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)


def leciona(professor_id, disciplina_id):
    return ProfessorDisciplina.query.filter_by(
        professor_id=professor_id,
        disciplina_id=disciplina_id
    ).first() is not None


class DisciplinaNaoEncontrada(Exception):
    pass

from flask import Blueprint, jsonify
from models import leciona_model

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor, id_disciplina):
    try:
        leciona = leciona_model.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except leciona_model.DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

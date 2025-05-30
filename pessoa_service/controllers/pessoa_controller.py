from flask import Blueprint, jsonify
from models import leciona_model
import requests
from services.professor_service import ProfessorService  


pessoa_bp = Blueprint('pessoa_bp', __name__)

def validar_professor(professor_id):
    resp = requests.get(f"https://projeto-api-jdan.onrender.com/professores/{professor_id}")
    return resp.status_code == 200


@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor, id_disciplina):
    try:
        leciona = leciona_model.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except leciona_model.DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

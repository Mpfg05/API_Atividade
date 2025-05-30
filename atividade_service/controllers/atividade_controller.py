from flask import Blueprint, jsonify, request
from ..models import atividade_model
from atividade_service.clients.pessoa_service_client import PessoaServiceClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET', 'POST'])
def atividades():
    if request.method == 'GET':
        atividades = atividade_model.listar_atividades()
        return jsonify(atividades)
    
    elif request.method == 'POST':
        data = request.get_json()
        
        professor = PessoaServiceClient.obter_professor(data.get('professor_id'))
        if not professor:
            return jsonify({'erro': 'Professor não encontrado'}), 404
            
        nova_atividade = atividade_model.criar_atividade(
            id_disciplina=data['id_disciplina'],
            enunciado=data['enunciado'],
            professor_id=data['professor_id']
        )
        
        return jsonify(nova_atividade), 201

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

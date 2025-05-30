atividades = []

class AtividadeNotFound(Exception):
    pass

def criar_atividade(id_disciplina, enunciado, professor_id):
    nova_atividade = {
        'id_atividade': len(atividades) + 1,
        'id_disciplina': id_disciplina,
        'professor_id': professor_id,
        'enunciado': enunciado,
        'respostas': []
    }
    atividades.append(nova_atividade)
    return nova_atividade

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

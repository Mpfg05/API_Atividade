
disciplinas = [
    {'nome': "apis e microservicos", 'id_disciplina': 1, 'alunos': [1, 2, 3, 4], 'professores': [1], 'publica': False},
    {'nome': "matematica financeira", 'id_disciplina': 2, 'alunos': [2], 'professores': [3], 'publica': True},
    {'nome': "matematica basica", 'id_disciplina': 3, 'alunos': [1, 2], 'professores': [3, 2], 'publica': False}
]

class DisciplinaNaoEncontrada(Exception):
    pass

def leciona(id_professor, id_disciplina):
    """Verifica se um professor leciona uma disciplina específica."""
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada
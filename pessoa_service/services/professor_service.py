import requests

class ProfessorService:
    BASE_URL = "https://projeto-api-jdan.onrender.com"
    
    @classmethod
    def obter_professor(cls, professor_id):
        try:
            response = requests.get(f"{cls.BASE_URL}/professores/{professor_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar professor: {e}")
            return None

    @classmethod
    def verificar_leciona(cls, id_professor, id_disciplina):
        try:
            response = requests.get(f"{cls.BASE_URL}/leciona/{id_professor}/{id_disciplina}")
            if response.status_code == 404:
                return False, 'Disciplina não encontrada'
            return response.json().get('leciona', False), ''
        except requests.RequestException as e:
            return False, f"Erro na comunicação: {e}"

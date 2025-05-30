import requests

class PessoaServiceClient:
    BASE_URL = 'http://localhost:5001'  

    @staticmethod
    def obter_professor(professor_id):
        resp = requests.get(f"{PessoaServiceClient.BASE_URL}/professores/{professor_id}")
        if resp.status_code == 200:
            return resp.json()
        return None

    @staticmethod
    def verificar_leciona(professor_id, disciplina_id):
        resp = requests.get(f"{PessoaServiceClient.BASE_URL}/professores/{professor_id}/leciona/{disciplina_id}")
        return resp.status_code == 200

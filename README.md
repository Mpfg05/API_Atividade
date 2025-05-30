## API de Atividades 

API Flask para gerenciamento de atividades acadêmicas, integrando serviços de professores e disciplinas.

## 📋 Estrutura do Projeto
API_Atividade/
├── atividade_service/
│ ├── controllers/
│ │ └── atividade_controller.py
│ ├── models/
│ │ └── atividade_model.py
│ ├── app.py
│ └── config.py
├── pessoa_service/
│ ├── controllers/
│ │ └── pessoa_controller.py
│ ├── models/
│ │ └── leciona_model.py
│ ├── app.py
│ └── config.py
├── requirements.txt
└── README.md



## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pip
- PostgreSQL (ou outro banco de dados configurável)

---
### Instalação
```bash
git clone https://github.com/Mpfg05/API_Atividade.git
cd API_Atividade
pip install -r requirements.txt
```

## Configuração
Renomeie .env.example para .env e configure as variáveis:

env
DATABASE_URL=postgresql://user:password@localhost:5432/atividade_db
FLASK_SECRET_KEY=sua_chave_secreta_aqui

---
## Iniciar Serviços
Abra dois terminais:

Terminal 1 (Atividade Service):

```bash
cd atividade_service
flask run --port 5001
Terminal 2 (Pessoa Service):
```

```bash
cd pessoa_service
flask run --port 5002
```
---
## 🔍 Endpoints Principais
-Atividade Service (:5001)
```POST /atividades - Cria nova atividade```

```GET /atividades/<id> - Busca atividade por ID```

```GET /atividades/professor/<id_professor> - Lista atividades por professor```

-Pessoa Service (:5002)
```POST /professores - Cadastra novo professor```

```GET /professores/<id> - Busca professor por ID```

## 🤝 Integração entre Serviços
A API de Atividades consulta a API de Pessoas para:

Validar existência de professores

Verificar se professor leciona disciplina

## 🛠️ Tecnologias Utilizadas
Flask

Flask-SQLAlchemy

PostgreSQL

Python-Dotenv

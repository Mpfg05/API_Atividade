## 📕 Controle de Atividades - API

Este repositório contém a API de Controle de Atividades, responsável por gerenciar as atividades vinculadas aos professores. A API permite cadastrar, listar e gerenciar atividades associadas aos IDs de professores fornecidos pela API do Sistema de Gerenciamento.

## 📋 Estrutura do Projeto
```
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
```
---

## 📖 Explicação da Arquitetura Utilizada

* Padrão de Arquitetura:
Estruturada com base no padrão MVC (Model-View-Controller), separando a lógica de dados, apresentação e controle.

* Banco de Dados:
Utiliza SQLite para a persistência de dados sobre as atividades e os vínculos com os professores.

* Integração com Sistema de Gerenciamento:
Esta API consome dados da API de Sistema de Gerenciamento, principalmente os IDs de professores, garantindo a consistência dos vínculos das atividades com os docentes.

* Rotas:
Implementa endpoints RESTful com suporte aos métodos HTTP GET e POST para manipulação dos recursos de atividades.

---

## 🔍 Descrição do Ecossistema de Microserviços
Este projeto integra um ecossistema de microserviços composto pelas seguintes APIs:

* Sistema de Gerenciamento:
Fornece dados de alunos, professores e turmas para os outros microserviços.

* Reservas:
Gerencia a reserva de salas de aula, integrando-se com a API do Sistema de Gerenciamento.

* Atividades (esta API):
Responsável pelo controle de atividades associadas aos professores, utilizando os IDs fornecidos pela API de Sistema de Gerenciamento.

A integração entre os microserviços ocorre através de comunicação via APIs RESTful, promovendo uma arquitetura modular e escalável, facilitando a manutenção e evolução do sistema.

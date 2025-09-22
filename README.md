# 📌 Web API Python – Arquitetura MVC + Clean Code

Este projeto é uma **Web API desenvolvida em Python**, estruturada na arquitetura **MVC (Model-View-Controller)** e seguindo princípios de **Clean Code** e **SOLID**.  

Foram aplicados conceitos como:  
- **Inversão de Dependência (DIP)**  
- **Injeção de Dependência (DI)**  
- **Testes unitários** para garantir confiabilidade  

## 🚀 Tecnologias Utilizadas
- **Python 3.11+**  
- **FastAPI** (criação da API)  
- **SQLAlchemy** (ORM e persistência)  
- **Pydantic** (validações e DTOs)  
- **pytest** (testes unitários)  
- **SQLite** (banco de dados para desenvolvimento)  

## 📂 Estrutura do Projeto

```bash
├── src
│ ├── controllers
│ ├── models
│ ├── views
│ ├── main
│ ├── validators
│ └── errors
├── tests
├── requirements.txt
└── README.md
```

## 💡 Conceitos Aplicados

### 🔄 Inversão de Dependência
Os services dependem de interfaces de repositório, não diretamente de implementações concretas.  
Isso garante baixo acoplamento e alta flexibilidade.  

### 🧪 Testes Unitários
Foram criados testes unitários com pytest, garantindo:  
- Validação das regras de negócio  
- Independência do banco de dados (mock de repositórios)  
- Confiabilidade da aplicação  

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/HenricoBirochi/PythonWebAPI_WithCleanCode
cd PythonWebAPI_WithCleanCode
```

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows

pip install -r requirements.txt
```

### 3. Rodar a aplicação

```bash
python3 run.py
```

A API estará disponível em: [http://localhost:3000](http://localhost:3000)

## 🧪 Rodando os Testes

```bash
pytest -v
```

## 📚 Exemplos de Endpoints
- `GET /user/find/<person_name>` → Busca usuário específico
- `POST /user` → Cria um usuário

## ✨ Próximos Passos
- Adicionar autenticação (JWT)
- Criar pipeline CI/CD para rodar testes automaticamente

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

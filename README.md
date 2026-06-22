# Módulo de Funcionários - Projeto Final 1º Bimestre
**Grupo 2:** Augusto, Patrick, Jonas, José Rocha

---

## Como rodar o projeto

### 1. Instalar o Django
```
pip install django
```

### 2. Entrar na pasta do projeto
```
cd funcionarios_project
```

### 3. Criar as tabelas no banco de dados
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Rodar o servidor
```
python manage.py runserver
```

### 5. Acessar no navegador
Abra: http://127.0.0.1:8000/funcionarios/listar

---

## Estrutura do projeto

```
funcionarios_project/
│
├── manage.py                      ← roda o servidor
├── requirements.txt               ← dependências
│
├── appfuncionarios/               ← configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── funcionarios/                  ← app principal (o módulo)
    ├── models.py       ← Cargo e Funcionario (banco de dados)
    ├── views.py        ← lógica de cada tela
    ├── urls.py         ← rotas/endereços
    ├── admin.py        ← painel admin
    ├── migrations/     ← histórico do banco
    └── templates/      ← telas HTML
        ├── base.html
        ├── login.html
        ├── listarFuncionarios.html
        ├── cadastroFuncionario.html
        ├── editarFuncionario.html
        ├── listarCargos.html
        ├── cadastroCargo.html
        └── editarCargo.html
```

---

## Rotas disponíveis
| URL | O que faz | Permissão necessária |
|-----|-----------|----------------------|
| `/login` | Tela de login | Pública |
| `/logout` | Encerra a sessão | Autenticado |
| `/funcionarios/listar` | Lista todos os funcionários | Autenticado |
| `/funcionarios/cadastro` | Cadastra novo funcionário | `add_funcionario` |
| `/funcionarios/editar/<id>` | Edita um funcionário | `change_funcionario` |
| `/funcionarios/excluir/<id>` | Exclui um funcionário | `delete_funcionario` |
| `/funcionarios/cargos` | Lista cargos | Autenticado |
| `/funcionarios/cadastroCargo` | Cadastra novo cargo | `add_cargo` |
| `/funcionarios/editarCargo/<id>` | Edita um cargo | `change_cargo` |

---

## API REST (para integração de outros grupos)

O módulo de Funcionários expõe uma API REST (Django REST Framework) para que outros sistemas consumam os dados de **funcionários** e **cargos**. A API exige autenticação por **token** — não é possível acessá-la sem um token válido.

### 1. Obter um token de acesso
Peça ao responsável pelo sistema (grupo Funcionários) para criar um usuário para o seu grupo. Em seguida, troque usuário/senha por um token:

```
POST /api/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:
```json
{ "token": "5d9585c5be82c5c37f52981d469e2c9aa136b8b2" }
```

Guarde esse token — ele não expira e deve ser enviado em todas as próximas requisições.

### 2. Usar o token nas requisições
Envie o header `Authorization` em toda chamada à API:
```
Authorization: Token 5d9585c5be82c5c37f52981d469e2c9aa136b8b2
```

### 3. Endpoints disponíveis

| Método | URL | O que faz |
|--------|-----|-----------|
| `GET` | `/api/funcionarios/` | Lista todos os funcionários |
| `POST` | `/api/funcionarios/` | Cria um funcionário |
| `GET` | `/api/funcionarios/<id>/` | Detalha um funcionário |
| `PUT` | `/api/funcionarios/<id>/` | Atualiza um funcionário (todos os campos) |
| `PATCH` | `/api/funcionarios/<id>/` | Atualiza parcialmente um funcionário |
| `DELETE` | `/api/funcionarios/<id>/` | Remove um funcionário |
| `GET` | `/api/cargos/` | Lista todos os cargos |
| `POST` | `/api/cargos/` | Cria um cargo |
| `GET` / `PUT` / `PATCH` / `DELETE` | `/api/cargos/<id>/` | Detalha/atualiza/remove um cargo |

Campos do `Funcionario`: `nome`, `cpf`, `email`, `telefone`, `data_admissao` (AAAA-MM-DD), `salario`, `cargo` (id do cargo).

### 4. Exemplo (curl)
```bash
curl -X POST http://augusto4d.pythonanywhere.com/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"seu_usuario","password":"sua_senha"}'

curl http://augusto4d.pythonanywhere.com/api/funcionarios/ \
  -H "Authorization: Token SEU_TOKEN_AQUI"
```

---

## Campos do Funcionário

- **Nome** – nome completo
- **CPF** – ex: 000.000.000-00
- **E-mail**
- **Telefone**
- **Data de Admissão**
- **Salário**
- **Cargo** – vinculado à tabela Cargo

---




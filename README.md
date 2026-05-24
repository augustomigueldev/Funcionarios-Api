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
        ├── listarFuncionarios.html
        ├── cadastroFuncionario.html
        ├── editarFuncionario.html
        ├── listarCargos.html
        └── cadastroCargo.html
```

---

## Rotas disponíveis

| URL | O que faz |
|-----|-----------|
| `/funcionarios/listar` | Lista todos os funcionários |
| `/funcionarios/cadastro` | Cadastra novo funcionário |
| `/funcionarios/editar/<id>` | Edita um funcionário |
| `/funcionarios/excluir/<id>` | Exclui um funcionário |
| `/funcionarios/cargos` | Lista cargos |
| `/funcionarios/cadastroCargo` | Cadastra novo cargo |

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




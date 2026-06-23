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

### 1. O que é o token e por que ele existe

Pensa no token como uma **senha temporária de acesso só pra API**, diferente da senha que você usa pra entrar no site (`/login`). São dois sistemas separados:

- **Login do site** (`/login`) → usado por **pessoas**, no navegador, pra ver as telas (HTML).
- **Token da API** (`/api/token/`) → usado por **outros programas/sistemas**, pra ler e mandar dados (JSON), sem precisar abrir nenhuma tela.

Fazer login no site **não gera token automaticamente**. São coisas independentes.

### 2. ⚠️ Erro mais comum: colar a URL no navegador NÃO funciona

Se você digitar `http://.../api/token/` na barra de endereço do navegador e apertar Enter, vai aparecer este erro:
```json
{"detail":"Método \"GET\" não é permitido."}
```
**Isso é esperado, não é um bug.** Toda vez que você cola uma URL e aperta Enter, o navegador só sabe fazer um pedido do tipo `GET` (que significa "me dá uma página pra eu ler"). Mas o endereço `/api/token/` só aceita um pedido do tipo `POST` (que significa "aqui estão uns dados, processa isso pra mim") — e ele exige que você envie usuário e senha junto. Não existe forma de "abrir" esse endereço só navegando, em nenhuma API do mundo. É preciso usar uma ferramenta que monte esse pedido `POST` por você.

### 3. Passo a passo para gerar o token (sem precisar instalar nada)

Abra o **PowerShell** (não o navegador!) e cole o comando abaixo, trocando `seu_usuario` e `sua_senha` pelos dados de um usuário que já existe no sistema:

```powershell
$resp = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/token/" -Method Post -Body @{username='seu_usuario';password='sua_senha'}
$resp
```

> Troque `http://127.0.0.1:8000` por `https://augusto4d.pythonanywhere.com` se quiser gerar o token no servidor de produção em vez do seu computador.

Se der certo, aparece assim na tela:
```
token
-----
5d9585c5be82c5c37f52981d469e2c9aa136b8b2
```

Esse texto longo de letras e números é o seu token. **Copie e guarde** — ele não expira e vai ser usado em todas as próximas chamadas à API.

**Se aparecer erro `400 Bad Request`** com a mensagem "Impossível fazer login com as credenciais fornecidas" → significa que o usuário ou a senha estão errados. Confirme com quem administra o sistema.

### 4. Como usar o token pra buscar dados

Ainda no PowerShell, com o `$resp` do passo anterior na memória, cole:

```powershell
$token = $resp.token
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/" -Headers @{Authorization="Token $token"}
```

Isso vai imprimir a lista de funcionários cadastrados, em formato de tabela/JSON. Se você fechar o PowerShell e abrir de novo, repita o passo 3 pra gerar o `$resp` antes de usar o passo 4 (a variável só existe enquanto a janela está aberta).

**Resumindo o conceito, em uma frase:** primeiro você "troca" usuário+senha por um token (passo 3, uma vez), depois usa esse token, no lugar de usuário+senha, em toda chamada futura (passo 4, sempre).

### 5. Usar o token nas requisições (formato genérico, pra qualquer linguagem/ferramenta)
Envie o header `Authorization` em toda chamada à API:
```
Authorization: Token 5d9585c5be82c5c37f52981d469e2c9aa136b8b2
```

### 6. Endpoints disponíveis

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

### 7. Como consumir cada operação, passo a passo

Em todos os exemplos abaixo, troque `SEU_TOKEN_AQUI` pelo token que você gerou no passo 3. E troque a URL base (`http://127.0.0.1:8000`) por `https://augusto4d.pythonanywhere.com` se for consumir o servidor de produção.

> Toda chamada à API precisa do header `Authorization: Token SEU_TOKEN_AQUI`. Sem ele, a resposta é `401 Unauthorized`.

#### GET — listar todos os funcionários
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/" -Headers @{Authorization="Token SEU_TOKEN_AQUI"}
```

#### GET — detalhar um funcionário específico (pelo id)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/1/" -Headers @{Authorization="Token SEU_TOKEN_AQUI"}
```

#### POST — criar um novo funcionário
```powershell
$body = @{
  nome="Maria Souza"; cpf="222.222.222-22"; email="maria@teste.com";
  telefone="11988887777"; data_admissao="2024-03-01"; salario="3500.00"; cargo=1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/" -Method Post `
  -Headers @{Authorization="Token SEU_TOKEN_AQUI"} -Body $body -ContentType "application/json"
```
O `cargo` é o **id** de um cargo já existente (veja em `/api/cargos/` quais ids existem).

#### PUT — atualizar um funcionário inteiro (precisa enviar todos os campos)
```powershell
$body = @{
  nome="Maria Souza"; cpf="222.222.222-22"; email="maria@teste.com";
  telefone="11988887777"; data_admissao="2024-03-01"; salario="4200.00"; cargo=1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/4/" -Method Put `
  -Headers @{Authorization="Token SEU_TOKEN_AQUI"} -Body $body -ContentType "application/json"
```

#### PATCH — atualizar só um campo (ex: só o salário)
```powershell
$body = @{ salario="5000.00" } | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/4/" -Method Patch `
  -Headers @{Authorization="Token SEU_TOKEN_AQUI"} -Body $body -ContentType "application/json"
```

#### DELETE — excluir um funcionário
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/funcionarios/4/" -Method Delete `
  -Headers @{Authorization="Token SEU_TOKEN_AQUI"}
```
Se funcionar, não volta nenhum texto na tela — isso é normal (significa `204 No Content`, ou seja, "deu certo e não tenho nada a mais pra te dizer").

#### Os mesmos exemplos em `curl` (Mac/Linux/Git Bash)
```bash
# Listar
curl http://127.0.0.1:8000/api/funcionarios/ -H "Authorization: Token SEU_TOKEN_AQUI"

# Criar
curl -X POST http://127.0.0.1:8000/api/funcionarios/ \
  -H "Authorization: Token SEU_TOKEN_AQUI" -H "Content-Type: application/json" \
  -d '{"nome":"Maria Souza","cpf":"222.222.222-22","email":"maria@teste.com","telefone":"11988887777","data_admissao":"2024-03-01","salario":"3500.00","cargo":1}'

# Atualizar (PUT)
curl -X PUT http://127.0.0.1:8000/api/funcionarios/4/ \
  -H "Authorization: Token SEU_TOKEN_AQUI" -H "Content-Type: application/json" \
  -d '{"nome":"Maria Souza","cpf":"222.222.222-22","email":"maria@teste.com","telefone":"11988887777","data_admissao":"2024-03-01","salario":"4200.00","cargo":1}'

# Excluir
curl -X DELETE http://127.0.0.1:8000/api/funcionarios/4/ -H "Authorization: Token SEU_TOKEN_AQUI"
```

### 8. Erros comuns e o que significam

| Resposta | O que significa | Como resolver |
|---|---|---|
| `401 Unauthorized` | Não enviou o token, ou ele está errado/mal formatado | Confira se o header é exatamente `Authorization: Token <token>` (com a palavra `Token` antes, e um espaço) |
| `400 Bad Request` ao gerar token | Usuário ou senha incorretos | Confirme as credenciais com o administrador do sistema |
| `404 Not Found` | O id do funcionário/cargo não existe, ou a URL está escrita errada (faltou a barra `/` no final) | Confira o id e se a URL termina com `/` |
| `405 Method Not Allowed` (ex: "Método GET não é permitido") | Você tentou acessar `/api/token/` digitando a URL no navegador | `/api/token/` só aceita `POST` — siga o passo 3 acima, não dá pra "abrir" essa URL |

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




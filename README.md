# 🛒 API de Lista de Compras

Api desenvolvida com o intuido de Gerenciar uma lista de Compras.

# 🚀 Funcionalidades do Projeto

Registro de Usuários: Criação de conta com senha
Criar Itens: Salva nome, quantidade e preço do produto.
Listar Itens: Exibe apenas os itens do usuário que está logado.
Atualizar Itens: Permite alterar quantidade, preço ou marcar como "Comprado".
Deletar Itens: Remove produtos da lista.

## ⚙️ Como Rodar o Projeto

1. Instalação
Abra o terminal na pasta do projeto e siga os passos:

1. Crie o ambiente virtual (opcional, mas recomendado)
python -m venv .venv

2. Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

3. Instale as dependências necessárias
pip install -r requirements.txt

## ⚙️ Como Texta se esta Funcionando ok

1. Ligue a Api
python app.py ou py app.py

2. Ligue o Arquivo teste_api.py
teste_api.py

Resultado experado Exemplo

--- INICIANDO TESTE AUTOMATIZADO ---

[1] Tentando registrar usuário 'aluno_teste'...
-> Tentativa de registro enviada.

[2] Fazendo Login...
-> Login OK! Token recebido: eyJhbGciOiJIUzI...

[3] Criando item 'Chocolate'...
-> Sucesso! Item criado: {'comprado': False, 'id': 4, 'nome': 'Chocolate', 'preco': 0.0, 'quantidade': 3}

[4] Listando itens do usuário...
-> Itens na lista: [{'comprado': False, 'id': 1, 'nome': 'Arroz', 'preco': 20.0, 'quantidade': 1}, {'comprado': False, 'id': 2, 'nome': 'Feizão', 'preco': 14.0, 'quantidade': 2}, {'comprado': False, 'id': 3, 'nome': 'Macarão', 'preco': 30.0, 'quantidade': 3}, {'comprado': False, 'id': 4, 'nome': 'Chocolate', 'preco': 0.0, 'quantidade': 3}]

[5] Deletando o item 4 para limpar...
-> Item deletado com sucesso!

--- FIM DOS TESTES: TUDO FUNCIONANDO! 🚀 ---

## ⚙️ Como Interagir com o Sistema

1. Configurando o Thunder Client

a. No VS Code, clique no ícone de Extensões (caixas na esquerda).
b. Instale o Thunder Client (ícone roxo com um raio).
c. Clique no ícone do Raio ⚡ na barra lateral e depois em New Request.

## 🧪 Parte 5: Roteiro de Testes (A Prova Real)

1. Cadastrar Usuário 👤

Método: Mude de GET para POST.
URL: http://127.0.0.1:5000/registro
Aba Body: Clique em Body → Selecione JSON (a palavra tem que ficar colorida).
Dados:
JSON
{ 
  "nome_usuario": "aluno_teste", 
  "senha": "123"
}

Ação: Clique em Send. (Sucesso: 201 Created).

2. Fazer Login (Pegar o Token) 🔑
Método: POST.
URL: http://127.0.0.1:5000/login
Body: Mantenha o mesmo JSON do passo anterior.
Ação: Clique em Send.

Sucesso: Status 200 OK. Vai aparecer um código gigante (ey...). Copie esse código (sem as aspas).

3. Criar Item (Usando o Token) 🛒
Método: POST.
URL: http://127.0.0.1:5000/itens
Aba Auth (O Pulo do Gato):
Clique na aba Auth.
Clique na opção Bearer.
Cole o código gigante no campo Token.
Aba Body (Os dados do item):
Volte para a aba Body.
Garanta que JSON está selecionado.
Cole os dados:
JSON
{ 
  "nome": "Macarrão",
  "quantidade": 3,
  "preco": 30.00
}
Ação: Clique em Send.

Sucesso: Status 201 Created (Mostrará o ID do item criado).
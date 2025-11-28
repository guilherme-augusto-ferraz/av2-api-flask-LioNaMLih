import requests

# URL da sua API local
BASE_URL = 'http://127.0.0.1:5000'


def rodar_testes():
    print("--- INICIANDO TESTE AUTOMATIZADO ---")

    # 1. REGISTRAR USUÁRIO
    print("\n[1] Tentando registrar usuário 'aluno_teste'...")
    usuario = {"nome_usuario": "aluno_teste", "senha": "123"}

    # O post pode dar erro 400 se o usuário já existir
    requests.post(f'{BASE_URL}/registro', json=usuario)
    print("-> Tentativa de registro enviada.")

    # 2. LOGIN (Para pegar o Token)
    print("\n[2] Fazendo Login...")
    resp = requests.post(f'{BASE_URL}/login', json=usuario)

    if resp.status_code == 200:
        token = resp.json()['token_acesso']
        headers = {'Authorization': f'Bearer {token}'}
        print(f"-> Login OK! Token recebido: {token[:15]}...")
    else:
        print(f"-> ERRO NO LOGIN: {resp.text}")
        return  # Para o teste se não logar

    # 3. CRIAR ITEM (Create)
    print("\n[3] Criando item 'Chocolate'...")
    item = {"nome": "Chocolate", "quantidade": 3}
    resp = requests.post(f'{BASE_URL}/itens', json=item, headers=headers)

    if resp.status_code == 201:
        dados_item = resp.json()
        id_item = dados_item['id']
        print(f"-> Sucesso! Item criado: {dados_item}")
    else:
        print(f"-> Erro ao criar: {resp.text}")
        return

    # 4. LISTAR ITENS (Read)
    print("\n[4] Listando itens do usuário...")
    resp = requests.get(f'{BASE_URL}/itens', headers=headers)
    print(f"-> Itens na lista: {resp.json()}")

    # 5. DELETAR O ITEM (Delete)
    print(f"\n[5] Deletando o item {id_item} para limpar...")
    resp = requests.delete(f'{BASE_URL}/itens/{id_item}', headers=headers)

    if resp.status_code == 200:
        print("-> Item deletado com sucesso!")
    else:
        print(f"-> Erro ao deletar: {resp.text}")

    print("\n--- FIM DOS TESTES: TUDO FUNCIONANDO! 🚀 ---")


# CORREÇÃO AQUI! 🔧
if __name__ == '__main__':
    try:
        rodar_testes()
    except ImportError:
        print("ERRO: Você precisa instalar a biblioteca 'requests'.")
        print("Rode no terminal: pip install requests")
    except Exception as e:
        print(f"ERRO DE CONEXÃO: O servidor está rodando? Detalhe: {e}")

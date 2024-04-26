import requests

# URL do servidor fornecido pelo professor para o registro de usuários
register_url = http://127.0.0.1:5000/register

# Dados do usuário a serem registrados
#user_data = {
#    "username": "teste",
#    "password": "teste"
#}

# Envia uma requisição POST para o servidor com os dados do usuário
response = requests.post(register_url, json=user_data)

# Verifica se a requisição foi bem-sucedida (código de status HTTP 201 indica sucesso)
if response.status_code == 201:
    print("Usuário registrado com sucesso!")
else:
    print("Erro ao registrar usuário:", response.json())


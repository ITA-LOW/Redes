import requests

register_url = "http://localhost:5000/register"

user_data = {
    "username": "seu_nome_de_usuario",
    "password": "sua_senha"
}

response = requests.post(register_url, json=user_data)

if response.status_code == 201:
    print("Usuário registrado com sucesso!")
else:
    print("Erro ao registrar usuário:", response.json())
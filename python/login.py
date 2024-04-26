import requests

# URL do servidor para login
login_url = "http://localhost:5000/login"

# Dados do usuário para login
login_data = {
    "username": "teste",
    "password": "teste"
}

# Envia uma requisição POST para o servidor com os dados de login
response = requests.post(login_url, json=login_data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrai o token JWT da resposta
    jwt_token = response.json().get('token')
    print("Login bem-sucedido! Token JWT obtido:", jwt_token)
else:
    print("Erro ao fazer login:", response.json())

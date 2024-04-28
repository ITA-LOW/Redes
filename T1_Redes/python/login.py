import requests

# URL da rota de login
login_url = "http://localhost:5000/login"

# Dados do usuário para login
user_data = {
    "username": "seu_nome_de_usuario",
    "password": "sua_senha"
}

# Envia uma requisição POST para fazer login
response = requests.post(login_url, auth=(user_data["username"], user_data["password"]))

# Verifica se o login foi bem-sucedido
if response.status_code == 200:
    try:
        # Extrai o token JWT da resposta e imprime
        token = response.json().get("token")
        print("Token JWT recebido:", token)
    except ValueError:
        print("Erro: Não foi possível analisar a resposta do servidor como JSON.")
else:
    # Imprime a mensagem de erro se o login falhou
    print("Erro ao fazer login:", response.text)

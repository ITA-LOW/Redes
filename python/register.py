import requests

####################################################### register ############################################
register_url = "http://192.168.31.75:80/register"
user_data_register = {
    "username": "seu_nome_de_usuario",
    "password": "sua_senha"
}
response = requests.post(register_url, json=user_data_register)

if response.status_code == 201:
    print("Usuário registrado com sucesso!")
else:
    print("Erro ao registrar usuário:", response.json())
#############################################################################################################

####################################################### login ###############################################
login_url = "http://192.168.31.75:80/login"

response = requests.post(login_url, auth=(user_data_register["username"], user_data_register["password"]))

# Verifica se o login foi bem-sucedido
if response.status_code == 200:
    try:
        # Extrai o token JWT da resposta
        token = response.json().get("access_token")
    except ValueError:
        print("Erro: Não foi possível analisar a resposta do servidor como JSON.")
else:
    # Imprime a mensagem de erro se o login falhou
    print("Erro ao fazer login:", response.text)
#############################################################################################################

####################################################### protected ###########################################
protected_url = "http://192.168.31.75:80/protected"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(protected_url, headers=headers)

if response.status_code == 200:
    print("Acesso à área protegida bem-sucedido!")
    print("Resposta:", response.json())
else:
    print("Erro ao acessar a área protegida:", response.json())
#############################################################################################################

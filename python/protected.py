import requests

# URL do serviço protegido fornecido pelo professor
protected_url = "http://127.0.0.1:5000/protected"

# Token JWT obtido no login
jwt_token = "seu_token_jwt_aqui"

# Cria o cabeçalho da requisição com o token JWT
headers = {"Authorization": "Bearer " + jwt_token}

# Envia uma requisição GET para o serviço protegido com o token JWT no cabeçalho
response = requests.get(protected_url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Acesso ao serviço protegido realizado com sucesso!")
    # Aqui você pode processar a resposta, se necessário
    print("Resposta do servidor:", response.json())
else:
    print("Erro ao acessar o serviço protegido:", response.json())

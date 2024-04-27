import requests

protected_url = "http://localhost:5000/protected"
token = "seu_token_aqui"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(protected_url, headers=headers)

if response.status_code == 200:
    print("Acesso à área protegida bem-sucedido!")
    print("Resposta:", response.json())
else:
    print("Erro ao acessar a área protegida:", response.json())

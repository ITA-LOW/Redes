from flask import Flask, request, jsonify
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ita'

# Simulando um banco de dados de usuários (pode ser substituído por um banco de dados real)
users = {}

# Função para verificar se o token JWT é válido
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token JWT ausente!'}), 401

        try:
            data = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'])
        except:
            return jsonify({'error': 'Token JWT inválido!'}), 401

        return f(*args, **kwargs)

    return decorated

# Rota para registro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    users[data['username']] = data['password']
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

# Rota para login e obtenção do token JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Credenciais inválidas!'}), 401

    username = data['username']
    password = data['password']

    if username not in users or users[username] != password:
        return jsonify({'error': 'Nome de usuário ou senha incorretos!'}), 401

    token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token}), 200

# Rota para acesso ao serviço protegido
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Você acessou o serviço protegido!'})

if __name__ == '__main__':
    app.run(debug=True)

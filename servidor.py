from flask import Flask, request, jsonify
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

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
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'error': 'Credenciais inválidas!'}), 401

    if auth.username not in users or users[auth.username] != auth.password:
        return jsonify({'error': 'Nome de usuário ou senha incorretos!'}), 401

    token = jwt.encode({'username': auth.username}, app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')}), 200

# Rota para acesso ao serviço protegido
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'Você acessou o serviço protegido!'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Dicionário para armazenar usuários registrados (usuário: senha)
registered_users = {}

# Rota para registro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    registered_users[username] = password
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

# Rota para login e obtenção do token JWT
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'error': 'Credenciais inválidas!'}), 401

    if auth.username not in registered_users or registered_users[auth.username] != auth.password:
        return jsonify({'error': 'Nome de usuário ou senha incorretos!'}), 401

    access_token = create_access_token(identity=auth.username)
    return jsonify({'token': access_token}), 200

# Rota para acesso ao serviço protegido
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)

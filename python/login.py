jwt = JWTManager(app)


# Esta rota é para o usuário se autenticar.
# Se o token expirar, ele terá que logar novamente.
# Você pode estabeler mecanismo de refresh automático do token.

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Username ou senha incorretos"}), 401
        # Você precisa proteger contra ataque de força bruta.
        # Pode contar quantas vezes um usuário tentou logar com erro.
        # e/ou pode enviar um CAPTCHA a ele.

    access_token = create_access_token(identity=username)

    # O default é retornar o token no corpo do request. 
    # O cliente tem que enviar um header "Authorization: Bearer <token>"

    return jsonify(access_token=access_token)
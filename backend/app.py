<<<<<<< HEAD
from flask import Flask, jsonify, request
=======
import os
from flask import Flask, request, jsonify
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea
from flask_cors import CORS
import os

app = Flask(__name__)

<<<<<<< HEAD
adm_login = [
    {
        "email": "expeditotaylor@gmailcom",
        "senha": "1234",
        "nome": "expedito"
    }
]

users_login = []

=======
# Libera CORS para seu frontend
CORS(app, supports_credentials=True)

# Usuário fixo para teste
USUARIO_FIXO = {
    "email": "teste",
    "password": "1234",
    "nome": "Usuário Teste"
}
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea

@app.route("/")
def home():
    return jsonify({"message": "Backend ativo!"})


<<<<<<< HEAD
@app.route("/login", methods=["POST"])
def Login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    for user in adm_login + users_login:
        if user["email"] == email and user["senha"] == senha:
            return jsonify({
                "success": True,
                "nome": user["nome"],
                "email": user["email"]
            })
=======
# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido"}), 400
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea

    email = data.get("email")
    password = data.get("password")

    if email == USUARIO_FIXO["email"] and password == USUARIO_FIXO["password"]:
        return jsonify({
            "success": True,
            "user": {
                "email": email,
                "nome": USUARIO_FIXO["nome"]
            }
        }), 200

    return jsonify({"success": False, "error": "Credenciais inválidas"}), 401


# REGISTRO
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    nome = data.get("nome")
    email = data.get("email")
    password = data.get("password")

    if not nome or not email or not password:
        return jsonify({"error": "Campos obrigatórios"}), 400

    # Aqui seria salvo no banco futuramente
    return jsonify({
<<<<<<< HEAD
        "success": False,
        "message": "E-mail ou senha inválidos"
    })


@app.route("/new", methods=["POST"])
def New():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")
    nome = dados.get("nome")

    # verifica se já existe
    for user in adm_login + users_login:
        if user["email"] == email:
            return jsonify({
                "success": False,
                "message": "E-mail já cadastrado"
            }), 400

    nova_conta = {
        "email": email,
        "senha": senha,
        "nome": nome
    }

    users_login.append(nova_conta)

    return jsonify({
        "success": True,
        "nome": nome,
        "email": email
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
=======
        "success": True,
        "message": "Usuário criado com sucesso",
        "user": {
            "nome": nome,
            "email": email
        }
    }), 201


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea

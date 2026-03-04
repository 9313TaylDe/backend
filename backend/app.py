import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Libera CORS para seu frontend
CORS(app, supports_credentials=True)

# Usuário fixo para teste
USUARIO_FIXO = {
    "email": "teste",
    "password": "1234",
    "nome": "Usuário Teste"
}

@app.route("/")
def home():
    return jsonify({"message": "Backend ativo!"})


# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido"}), 400

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

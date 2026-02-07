from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users_credentials = [
    {
        "email": "teste@gmail.com",
        "senha": "1234",
        "nome": "joao"
    }
]

adm_credentials = [
    {
        "email": "admin@gmail.com",
        "senha": "1234",
        "nome":"Expedito"
      
    }
]

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    for user in adm_credentials + users_credentials:
        if user["email"].lower() == email.lower() and user["senha"] == senha:
            return jsonify({
                "success": True,
                "nome": user["nome"],   # 👈 vem do backend
                "email": user["email"]
            })

    return jsonify({
        "success": False,
        "message": "Usuário ou senha inválidos"
    }), 401

@app.route("/new", methods=["POST"])
def New_Account():
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    for user in users_credentials:
        if email == user["email"]:
            return jsonify({"success": False, "message": "Conta já cadastrada"})

    users_credentials.append({
        "nome": nome,
        "email": email,
        "senha": senha
    })

    return jsonify({"success": True})


@app.route("/logout", methods=["POST"])
def Logout():
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


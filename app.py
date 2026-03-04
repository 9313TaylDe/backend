from flask import Flask, jsonify, request
from flask_cors import CORS
import os
<<<<<<< HEAD

=======
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea
app = Flask(__name__)
CORS(app)

adm_login = [
    {
        "email": "expeditotaylor@gmailcom",
        "senha": "1234",
        "nome": "expedito"
    }
]

users_login = []


@app.route("/")
def home():
    return jsonify({"message": "Backend ativo!"})


@app.route("/login", methods=["POST"])
def Login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    for user in adm_login + users_login:
        if user["email"] == email and user["senha"] == senha:
            return jsonify({
<<<<<<< HEAD
                "success": True,
                "nome": user["nome"],
                "email": user["email"]
            })

    return jsonify({
        "success": False,
        "message": "E-mail ou senha inválidos"
    })


=======
    "success": True,
    "nome": nome,
    "email": email
})
    return jsonify({"success":False, "message":"E-mail ou senha inválidos"})
        
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea
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
<<<<<<< HEAD

    return jsonify({
        "success": True,
        "nome": nome,
        "email": email
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
=======
    return jsonify({
    "success": True,
    "nome": nome,
    "email": email
})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> 8f43412cf68f707da89832ecffc78970a9f2b9ea

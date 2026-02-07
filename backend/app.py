from flask import Flask, jsonify, request
from flask_cors import CORS
import cors from "cors";
app.use(cors({
  origin: "https://meu-portifolio-six-iota.vercel.app",
  credentials: true,
}));

app = Flask(__name__)
CORS(app)

adm_login = [
    {"email": "expeditotaylor@gmailcom", 
     "senha":"1234",
     "nome":"expedito"}
]

users_login = [
  
]


@app.route("/login", methods=["POST"])
def Login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")
    
    for user in adm_login + users_login:
        if user["email"] == email and user["senha"] == senha:
            return jsonify({"success":True, "nome":user["nome"],"email":user["email"]})
    return jsonify({"success":False, "message":"E-mail ou senha inválidos"})
        
@app.route("/new", methods=["POST"])
def New():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")
    nome = dados.get("nome")
    nova_conta = {
        "email": email,"senha" : senha, "nome": nome
        
    }
    users_login.append(nova_conta)
    return jsonify({"success":True, "nome":nome["nome"],"email":email["email"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


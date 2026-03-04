from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Permitir CORS para seu frontend rodando em Vercel
CORS(app, origins=["https://meu-portifolio-six-iota.vercel.app"])

@app.route('/')
def home():
    return jsonify({ "message": "Backend ativo!" })

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Aqui você pode verificar usuário/senha
    if email == "teste" and password == "1234":
        return jsonify({"success": True, "message": "Logado com sucesso"})
    else:
        return jsonify({"success": False, "message": "Credenciais inválidas"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# LIBERA CORS COMPLETAMENTE (para testar)
CORS(app, supports_credentials=True)

@app.route("/")
def home():
    return jsonify({"message": "Backend ativo!"})

@app.route("/login", methods=["POST", "OPTIONS"])
def login():

    # Responde ao preflight
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if email == "teste" and password == "1234":
        return jsonify({"success": True})

    return jsonify({"success": False}), 401


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

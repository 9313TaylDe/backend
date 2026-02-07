from flask import Flask, jsonify,request
from flask_cors import CORS
import os
import pygame


app = Flask(__name__)
CORS(app)
PASTA = os.path.abspath("/src/musics")
indice  = 0 
pausada = False
lista = []
print("Mixer inicializado:", pygame.mixer.get_init())
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
for diretorio,pasta,arquivo in os.walk(PASTA):
    for arquivos in arquivo:
        if arquivos.endswith((".mp3",".mp4",".wav",".flac")):
            lista.append(os.path.join(pasta,arquivos))
    

def Musicas():
   for musica in lista:
       return lista
   return jsonify({"musicas": "musicas"})

@app.route("/play/<int:i>", methods=["GET"])
def PlayMusic(i):
    global indice,pausada
    if not lista:
        return jsonify({"Erro": "Nao ha musicas no repositorio"})
    
    try:
        musica = lista[i % len(lista)]
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()
        pausada= False
        return jsonify({"Tocando": os.path.basename(lista[i])})
    except Exception as e:
        return str(e)
            
if __name__ == "__main__":
    app.run(debug=True)
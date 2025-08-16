from flask import Flask, jsonify
import requests
import html
import random

app = Flask(__name__)
def obtener_pregunta():
    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"    
    response = requests.get(url)
    data = response.json()

    if data["response_code"] == 0:
        pregunta = html.unescape(data["results"][0]["question"])
        correcta = html.unescape(data["results"][0]["correct_answer"])
        incorrectas = [html.unescape(ans) for ans in data["results"][0]["incorrect_answers"]]

        opciones = incorrectas + [correcta]
        random.shuffle(opciones)

        return {
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta_correcta": correcta
        }
    else:
        return None
    
    @app.route("/trivia", methods=["GET"])
    def trivia():
        pregunta = obtener_pregunta()
    if pregunta:
        return jsonify(pregunta)
    else:
        return jsonify({"error": "No se pudo obtener pregunta"}), 500
    
    @app.route("/", methods=["GET"])
    def home():
        return "<h1>API de Trivia 🎲</h1><p>Usa el endpoint <b>/trivia</b> para obtener una pregunta.</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

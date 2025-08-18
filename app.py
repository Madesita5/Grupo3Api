from flask import Flask, render_template, request

app = Flask(__name__)

# Preguntas y respuestas correctas
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["París", "Londres", "Madrid", "Berlín"],
        "respuesta_correcta": "París"
    },
    {
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": ["Venus", "Mercurio", "Marte", "Júpiter"],
        "respuesta_correcta": "Mercurio"
    },
    {
        "pregunta": "¿Cuál es 5 + 7?",
        "opciones": ["10", "12", "11", "13"],
        "respuesta_correcta": "12"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        puntaje = 0
        respuestas_usuario = []
        for i in range(len(preguntas)):
            resp = request.form.get(f"pregunta{i}")
            respuestas_usuario.append(resp)
            if resp == preguntas[i]["respuesta_correcta"]:
                puntaje += 1
        return render_template("resultado.html", puntaje=puntaje, total=len(preguntas),
                               respuestas=respuestas_usuario, preguntas=preguntas)
    return render_template("index.html", preguntas=preguntas)


# Feature de estadisticas
@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    texto = request.args.get("texto", "")

    resultado = None
    if texto:
        num_palabras = len(texto.split())
        num_caracteres = len(texto.replace(" ", ""))
        num_vocales = sum(1 for c in texto.lower() if c in "aeiouáéíóú")

        resultado = {
            "palabras": num_palabras,
            "caracteres": num_caracteres,
            "vocales": num_vocales
        }

    return render_template("estadisticas.html", resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

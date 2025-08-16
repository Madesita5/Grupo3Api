from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 100},
    {"id": 2, "nombre": "Producto 2", "precio": 200},
]

@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

@app.route('/productos', methods=['POST'])
def add_producto():
    new_producto = request.get_json()
    if 'nombre' not in new_producto or 'precio' not in new_producto:
        return jsonify({"error": "Faltan campos requeridos: nombre y precio"}), 400

    productos.append(new_producto)
    return jsonify(new_producto), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

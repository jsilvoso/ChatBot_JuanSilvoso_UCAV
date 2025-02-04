from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)
    return jsonify({"response": response})

def generate_response(user_input):
    responses = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "adiós": "¡Hasta luego!",
        "cómo estás": "Estoy bien, gracias por preguntar.",
        "me dices una receta": "¿Cuál quieres? ¿De comida o de postre?"
    }
    return responses.get(user_input.lower(), "Lo siento, no entiendo esa pregunta.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



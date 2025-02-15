#Programa principal
#Primera Versión: "Se genera una respuesta si la pregunta coincide con alguna de las establecidas"

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista global para almacenar el historial
chat_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = generate_response(user_input)

    # Guardamos el mensaje del usuario y la respuesta del chatbot
    chat_history.append({"user": user_input, "bot": response})

    return jsonify({"response": response, "history": chat_history})

def generate_response(user_input):
    responses = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "hello": "Hello, a ti también",
        "adiós": "¡Hasta luego!",
        "cómo estás": "Estoy bien, gracias por preguntar."
    }
    return responses.get(user_input.lower(), "Lo siento, no entiendo esa pregunta.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




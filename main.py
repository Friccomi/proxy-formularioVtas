from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Dirección del Apps Script que recibe el POST
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxAYEoskZUGluDMxhfhCIqsTy_r-QQFarZGK7rB_2FH6YZWEG68vAIM_5jkVJIu7aGE/exec"

@app.route("/enviar", methods=["POST"])
def reenviar_datos():
    try:
        # Reenvía el JSON recibido al Apps Script
        response = requests.post(GOOGLE_SCRIPT_URL, json=request.json)

        # Devuelve el contenido tal como vino de Google
        return (response.text, response.status_code, {'Content-Type': 'application/json'})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500



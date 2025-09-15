from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycbwUjG8neViyQwtgkozuzOOE4m3TTwOf1sIjWFevQueedoixESxQ7-hFVG_OOi3UnOmr/exec"  # tu URL real

@app.route('/proxy', methods=['POST', 'OPTIONS'])
def proxy():
    if request.method == 'OPTIONS':
        # CORS preflight
        response = app.make_default_options_response()
        headers = response.headers
        headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Allow-Headers'] = 'Content-Type'
        headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        return response

    data = request.get_json()
    try:
        r = requests.post(GAS_ENDPOINT, json=data)
        r.raise_for_status()
        return jsonify(ok=True, response=r.text)
    except Exception as e:
        import traceback
        traceback.print_exc()  # Esto imprime el stack trace completo
        return jsonify(ok=False, error=str(e)), 500

# CORS global (opcional)
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5000)

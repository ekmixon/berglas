import os

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def f():
    api_key = os.environ.get('API_KEY')
    tls_key_path = os.environ.get('TLS_KEY')

    tls_key = "file does not exist"
    if tls_key_path and os.path.isfile(tls_key_path):
        tls_key = open(tls_key_path, "r").read()

    body = f"API_KEY: {api_key}\nTLS_KEY_PATH: {tls_key_path}\nTLS_KEY: {tls_key}"

    return Response(response=body, status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

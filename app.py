from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Flask activo para MyCase OAuth."

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"""
    <h1>Authorization Code Recibido</h1>
    <p>Código: <code>{code}</code></p>
    <p>Copia este código para intercambiarlo por un access_token.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/consultar_cep/<cep>/")
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"erro": "CEP inválido"})

if __name__ == "__main__":
    app.run(debug=True)

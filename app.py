from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

DEEPSEEK_API_KEY = "sk-b69ca9e0fcad4e5e8ab3ec8882c75426"
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.json
    pergunta = data.get("mensagem")

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": pergunta}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }

    response = requests.post(DEEPSEEK_URL, json=payload, headers=headers)

    if response.status_code == 200:
        resposta = response.json()['choices'][0]['message']['content']
        return jsonify({"resposta": resposta})
    else:
        return jsonify({"erro": "Erro ao consultar a API"}), 500

if __name__ == '__main__':
    app.run(debug=True)

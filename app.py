from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '7117423200:AAEeFkUOoPxux_8Q_IiC_8OchTVSpG2356Y'
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data or 'message' not in data:
        return "no message", 200

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    reply = f"شما گفتید: {text}"

    payload = {
        "chat_id": chat_id,
        "text": reply
    }

    requests.post(URL, data=payload)
    return "ok", 200

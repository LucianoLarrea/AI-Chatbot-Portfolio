import os
import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    user_input = request.values.get("Body", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    
    twilio_response = MessagingResponse()
    twilio_response.message(response["choices"][0]["message"]["content"])
    return str(twilio_response)

if __name__ == "__main__":
    app.run(port=5000)

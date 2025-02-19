# 🛠 Multi-Channel AI Chatbot

This chatbot allows users to interact through multiple platforms such as **Telegram, WhatsApp, and Web**.

---

## 📌 Project Structure
```
AI-Chatbot-Portfolio/
│── 05_multichannel_ai/
│   ├── app.py  # Main API with FastAPI
│   ├── telegram_bot.py  # Telegram integration
│   ├── whatsapp_bot.py  # WhatsApp integration (Twilio)
│   ├── requirements.txt  # Dependencies
│   ├── README.md  # Documentation
```

---

## ✅ Installation & Setup  
### 1️⃣ Install Dependencies  
```bash
pip install fastapi uvicorn openai requests python-telegram-bot twilio
```

### 2️⃣ Configure Environment Variables  
Obtain the following credentials and add them to a `.env` file:  
```
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+123456789
YOUR_WHATSAPP_NUMBER=whatsapp:+987654321
```

---

## 🚀 How to Run

### 1️⃣ Run the FastAPI server
```bash
uvicorn app:app --reload
```

### 2️⃣ Start the Telegram bot
```bash
python telegram_bot.py
```

### 3️⃣ Start the WhatsApp bot
```bash
python whatsapp_bot.py
```

---

## 🛠 Features
- **Multi-Platform:** Supports Telegram, WhatsApp, and REST API.
- **Powered by OpenAI:** Uses GPT for intelligent responses.
- **Easy Deployment:** Runs on FastAPI and Flask.
- **Scalable:** Can integrate with more messaging platforms.

---

## 📬 Contact
- **GitHub:** https://github.com/LucianoLarrea
- **Email:** takticflow@gmail.com

---

🔹 *This project is part of my AI Chatbot Portfolio. Stay tuned for updates!* 🚀

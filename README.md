# 🌐 Multilingual Intelligent Chatbot

This is a Streamlit-based chatbot app that lets you chat in any language! Your message gets translated to English, processed by a chatbot model, and the response is translated back to your language — creating an interactive multilingual assistant.

<p align="center">
  <img src="https://img.shields.io/badge/streamlit-1.30.0-brightgreen" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
</p>

---

✅ **Features**

- Chat with an AI assistant in **any language**
- Automatic language detection & translation
- Uses Azure Translator for accurate translations
- Intelligent chatbot responses using BlenderBot
- Beautiful Streamlit interface with a fixed input box and emoji send button
- Conversation history saved within the chat window

---

🚀 **Requirements**

- Python 3.8+
- Azure Translator resource & keys ([Azure Translator Docs](https://learn.microsoft.com/azure/cognitive-services/translator/quickstart-translator?tabs=csharp))
- Internet connection (for Azure API + model downloads)

**Python Packages**

Install all dependencies with:

```bash
pip install -r requirements.txt

requirements.txt

streamlit
requests
torch
transformers

🛠 Setup

1️⃣ Clone this repository:

bash

git clone https://github.com/yourusername/multilingual-chatbot.git
cd multilingual-chatbot
2️⃣ Set your Azure Translator credentials as environment variables:

On Windows CMD/PowerShell:

powershell

setx AZURE_TRANSLATOR_KEY "your-azure-key"
setx AZURE_TRANSLATOR_ENDPOINT "your-endpoint-url"
On macOS/Linux:

bash

export AZURE_TRANSLATOR_KEY="your-azure-key"
export AZURE_TRANSLATOR_ENDPOINT="your-endpoint-url"
3️⃣ Run the app:

bash

streamlit run app.py
💬 Usage

Open your browser to http://localhost:8501

Type a message in any language at the bottom chat box.

Click the ➤ (send) button or press Enter.

Enjoy a real-time conversation with a multilingual AI assistant!

This project is for educational use only. See LICENSE file for details.

🙌 Credits

Built with Streamlit

Uses Azure Translator for language detection & translation

Powered by BlenderBot via Hugging Face Transformers

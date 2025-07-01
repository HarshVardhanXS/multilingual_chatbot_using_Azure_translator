import streamlit as st
import requests
import os
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load Azure Translator info
AZURE_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
assert AZURE_KEY and AZURE_ENDPOINT, "Set AZURE_TRANSLATOR_KEY and AZURE_TRANSLATOR_ENDPOINT"

# BlenderBot model
st.write("🧠 Loading BlenderBot model...")
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
st.write("✅ BlenderBot model ready.")

def detect_language(text):
    url = f"{AZURE_ENDPOINT}/detect?api-version=3.0"
    headers = {"Ocp-Apim-Subscription-Key": AZURE_KEY, "Content-Type": "application/json"}
    body = [{"text": text}]
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()[0]["language"]

def translate_text(text, target_lang):
    url = f"{AZURE_ENDPOINT}/translate?api-version=3.0&to={target_lang}"
    headers = {"Ocp-Apim-Subscription-Key": AZURE_KEY, "Content-Type": "application/json"}
    body = [{"text": text}]
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()[0]["translations"][0]["text"]

def get_chatbot_response(english_text):
    inputs = tokenizer(english_text, return_tensors="pt")
    reply_ids = model.generate(**inputs, max_length=200)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return reply

# Streamlit UI
st.title("🤖 Multilingual BlenderBot Chatbot")
st.markdown("Chat in any language – I'll translate, understand, and reply intelligently!")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    user_lang = detect_language(user_input)
    st.session_state.history.append(("You", user_input))

    text_in_english = translate_text(user_input, "en")
    bot_response_en = get_chatbot_response(text_in_english)
    bot_response_translated = translate_text(bot_response_en, user_lang)

    st.session_state.history.append(("Bot (EN)", bot_response_en))
    st.session_state.history.append((f"Bot ({user_lang.upper()})", bot_response_translated))

# Display conversation history
st.markdown("📝 Conversation History")
for speaker, text in st.session_state.history:
    st.markdown(f"**{speaker}:** {text}")

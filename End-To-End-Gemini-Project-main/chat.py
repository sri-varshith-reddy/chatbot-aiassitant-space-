import pyttsx3
import speech_recognition as sr
import streamlit as st
import threading

# Initialize Text-to-Speech Engine
def init_tts_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1)  
    return engine

tts_engine = init_tts_engine()

# Function to speak text in a separate thread
def speak_text(text):
    def speak():
        tts_engine.say(text)
        tts_engine.runAndWait()
    
    tts_thread = threading.Thread(target=speak)
    tts_thread.start()

# Function to listen to user input
def listen_for_input():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service."
    except AttributeError:
        return "PyAudio not found. Please install PyAudio."

# Function to generate responses (dummy implementation)
def generate_response(user_input):
    responses = {
        "help": "I can assist with space-related queries. What do you need help with?",
        "moon": "The Moon is Earth's only natural satellite. It influences tides and has been visited by astronauts.",
        "mars": "Mars is known as the Red Planet due to its reddish appearance. It has the largest volcano in the solar system.",
        "black hole": "A black hole is a region of space where gravity is so strong that not even light can escape from it.",
        "stop": "Goodbye! Ending the chat."
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that. Can you please clarify?")

# Function to handle voice input in a separate thread
def handle_voice_input():
    while True:
        user_input = listen_for_input().lower()
        if "stop" in user_input:
            speak_text("Goodbye! Ending the chat.")
            st.session_state['chat_active'] = False
            break
        
        response = generate_response(user_input)
        speak_text(response)
        st.session_state['chat_history'].append(f"User: {user_input}")
        st.session_state['chat_history'].append(f"Assistant: {response}")

# Streamlit app setup
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #000814;
        color: #eaeaea;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #00a8e8;
        color: white;
        border-radius: 10px;
    }
    .stTextInput input {
        background-color: #001d3d;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Astronaut Assistant")

if 'chat_active' not in st.session_state:
    st.session_state['chat_active'] = True
    st.session_state['chat_history'] = []

# Text input
with st.form(key='text_input_form'):
    user_text_input = st.text_input("Type your message here (e.g., 'tell me about the moon')", key='input_text')
    submit_text = st.form_submit_button("Submit")

    if submit_text:
        if user_text_input.strip().lower() == "stop":
            speak_text("Goodbye! Ending the chat.")
            st.session_state['chat_active'] = False
        else:
            response = generate_response(user_text_input)
            speak_text(response)
            st.session_state['chat_history'].append((f"User: {user_text_input}", "#00a8e8"))
            st.session_state['chat_history'].append((f"Assistant: {response}", "#f77f00"))

# Display chat history with colors
st.markdown("<h3 style='color: #00a8e8;'>Chat History:</h3>", unsafe_allow_html=True)
chat_container = st.container()

if st.session_state['chat_history']:
    for chat, color in st.session_state['chat_history']:
        chat_container.markdown(f"<p style='color:{color};'>{chat}</p>", unsafe_allow_html=True)

# Voice input
if st.session_state['chat_active']:
    if st.button("Start Voice Interaction"):
        threading.Thread(target=handle_voice_input, daemon=True).start()

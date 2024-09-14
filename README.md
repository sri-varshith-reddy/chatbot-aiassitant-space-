
🚀 Astronaut Assistant
Overview
The Astronaut Assistant is a Streamlit-based application that integrates text-to-speech (TTS) and speech recognition to provide an interactive assistant experience. It supports both text and voice input, making it versatile for different user preferences. This assistant can answer space-related queries and provide responses using voice feedback.

Features
Text-to-Speech (TTS): Converts text responses into spoken words.
Speech Recognition: Listens to and processes user speech.
Text Input: Allows users to type queries and receive responses.
Voice Input: Users can start voice interaction to ask questions.
Chat History: Displays a record of user and assistant interactions.
Installation
To get started, ensure you have Python installed. Then, install the required packages:

bash
Copy code
pip install pyttsx3 SpeechRecognition streamlit
Note: For speech recognition to work, you need to install pyaudio. You can do this via pip:

bash
Copy code
pip install pyaudio
Usage
Run the Application:

Start the Streamlit app using:

bash
Copy code
streamlit run app.py
Interact with the Assistant:

Text Input: Type your message in the input box and submit.
Voice Input: Click "Start Voice Interaction" to begin listening for voice commands.
Stopping Interaction:

Type "stop" or click the stop button in voice mode to end the chat session.

Code Explanation
init_tts_engine(): Initializes and configures the TTS engine.
speak_text(text): Speaks the given text using the TTS engine in a separate thread.
listen_for_input(): Listens for audio input from the user and converts it to text.
generate_response(user_input): Provides responses based on predefined keywords.
handle_voice_input(): Continuously listens for voice input and generates responses.
Customization
Responses: Modify the generate_response function to add or change responses.
Styling: Update the HTML/CSS in the st.markdown call to adjust the appearance of the app.
Troubleshooting
PyAudio Errors: Ensure PyAudio is installed properly. If issues persist, refer to the PyAudio installation guide.
Voice Recognition Errors: Check microphone settings and ensure your system's audio input is functioning correctly.

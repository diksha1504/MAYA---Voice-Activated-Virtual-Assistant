MAYA - Voice-Activated Virtual Assistant

Maya is a voice-activated virtual assistant designed to perform tasks such as web browsing, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model.  
It acts as a smart companion, similar to Alexa or Google Assistant.


Features
- Voice Recognition  
  - Listens for commands using the speech_recognition library.  
  - Activates when the wake word "Maya" is detected.

- Text-to-Speech (TTS)  
  - Converts responses into natural speech using pyttsx3.  
  - Supports gTTS + pygame for smoother playback.

- Web Browsing  
  - Opens websites like Google, YouTube, Facebook, LinkedIn via voice commands.

- Music Playback  
  - Interfaces with a custom musicLibrary module to stream songs from web links.

- News Fetching  
  - Uses NewsAPI to fetch and read the latest headlines.

- OpenAI Integration  
  - Uses GPT-3.5-turbo for handling complex queries.  
  - Can answer questions, summarize information, and act as a general-purpose assistant.



Workflow
1. Initialization → Greets user with "Initializing Maya…"  
2. Wake Word Detection → Listens for "Maya" and activates  
3. Acknowledgment → Responds with "Ya"  
4. Command Processing → Identifies whether to open a website, play music, fetch news, or answer with GPT-3.5  
5. Speech Output → Provides natural responses with TTS


Libraries Used
- speech_recognition – voice input  
- webbrowser – for web navigation  
- pyttsx3 – local text-to-speech  
- musicLibrary – custom music handling  
- requests – API calls (NewsAPI, OpenAI)  
- openai – AI query handling  
- gTTS – text-to-speech via Google  
- pygame – audio playback  
- os – system handling  


Future Improvements
- Add calendar and reminder integration  
- Smart home IoT control  
- Continuous conversation without repeating wake word  
- Offline mode with local LLMs  



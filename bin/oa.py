import os

from dotenv import load_dotenv
import openai

load_dotenv()
WHISPER_MODEL = "whisper-1"
openai.api_key = os.environ["OPENAI_API_KEY"]


def transcribe_whisper(filepath: str) -> str:
    with open(filepath, "rb") as audio_file:
        response = openai.Audio.transcribe(WHISPER_MODEL,
                                           audio_file,
                                           prompt="Hello, this is a properly structured message. GPT, ChatGPT.")
    transcript = response["text"]
    return transcript

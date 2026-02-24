import os
from dotenv import load_dotenv
from google.adk.models import Gemini

load_dotenv()

geminiModel = Gemini(
    model="gemini-1.5-flash",
    api_key=os.getenv("AIzaSyBelbMxG2KHBW2FBeD6w_bbb4QGezNn9kU")
)
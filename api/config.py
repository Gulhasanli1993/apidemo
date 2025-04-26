from dotenv import load_dotenv
import os

load.dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in env fie.")
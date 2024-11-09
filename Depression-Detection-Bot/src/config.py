from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
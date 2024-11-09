import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access credentials from environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
password = os.getenv('PASSWORD')
user_agent = os.getenv('USER_AGENT')
username = os.getenv('USERNAME')

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username
)

try:
    print(f"Logged in as: {reddit.user.me()}")
except Exception as e:
    print(f"Error: {e}")

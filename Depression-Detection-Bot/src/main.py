from config import client_id, client_secret, user_agent, username, password
from model import detect_depression
import praw
import logging

# Set up logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

# Set up Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

# Monitor posts in subreddit
subreddit_name = "mentalhealth"
subreddit = reddit.subreddit(subreddit_name)

for post in subreddit.stream.submissions():
    title = post.title
    content = post.selftext
    full_text = f"{title} {content}"

    if detect_depression(full_text):
        logging.info(f"Depression detected in post ID: {post.id}")
        post.reply("Hello! This message is being sent by a bot. If you're feeling down, please consider reaching out to a mental health professional. You’re not alone!")

import feedparser
import requests
import time
from pyrogram import Client
import datetime


# Telegram bot API key and channel name
API_ID = ''
API_HASH = ''
BOT_TOKEN = ''
channel_id = ''

# Create the Telegram bot
app = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

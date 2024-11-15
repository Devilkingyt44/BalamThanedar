import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import random
import string

# Set up logging to track the bot's actions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token (replace with your bot's token)
API_TOKEN = 'YOUR_BOT_API_TOKEN'
# Admin's Telegram user ID (replace with your admin's user ID)
ADMIN_ID = 'YOUR_ADMIN_USER_ID'

# Function to generate a random link (mocking link shortening)
def generate_link():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'https://example.com/{random_string}'

# Function to log the IP address of the user who clicks the link (fictional)
def log_ip_address(ip):
    with open("log.txt", "a") as log_file:
        log_file.write(f"IP Address: {ip}\n")

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hello {user.first_name}, I am ShadowFlux bot! Use /generate to get your link.")

# Command to generate a short URL and track the IP
def generate(update: Update, context: CallbackContext) -> None:
    # Generate the link
    link = generate_link()
    
    # Send the link to the user
    update.message.reply_text(f"Here is your link: {link}")
    
    # Send the IP address to the admin (fictional IP used for this example)
    user_ip = '192.168.1.1'  # Replace with a real IP grabber logic if needed
    log_ip_address(user_ip)
    context.bot.send_message(chat_id=ADMIN_ID, text=f"New IP address captured: {user_ip}")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(API_TOKEN)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Register the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

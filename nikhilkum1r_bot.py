import os
import telebot
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Check if the BOT_TOKEN is available
if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
    exit()

# Create a TeleBot instance with the obtained token
bot = telebot.TeleBot(BOT_TOKEN)


# Define command handlers
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'Hello User!')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, 'I am Nikhil! Please type something so I can respond!')


@bot.message_handler(commands=['custom'])
def custom_command(message):
    bot.reply_to(message, 'This is a custom command!')


# Define response handling function
def handle_response(text):
    greetings = ["hi", "hello", "hey", "greetings"]
    compliments = ["great", "awesome", "fantastic", "amazing"]
    topics = ["Python", "programming", "coding", "AI", "machine learning", "data science"]
    farewell = ["goodbye", "bye", "see you later", "farewell"]
    affirmations = ["yes", "yeah", "yep", "indeed", "absolutely"]
    negations = ["no", "nope", "nah", "not really"]
    thanks = ["thank you", "thanks", "appreciate it"]
    advice = ["try to debug it", "read the documentation", "ask for help on forums"]
    
    if text.lower() in greetings:
        return random.choice(["Hello!", "Hi there!", "Hey!"])
    elif text.lower() == "help":
        return 'Hey there! ' + bot.get_me().username
    elif text.lower() == "start":
        return 'Welcome to the chat!'
    elif text.lower() == 'how are you?':
        return 'I\'m doing great!'
    elif text.lower() == 'i love python':
        return 'That\'s awesome! I also love Python.'
    elif any(word in text.lower() for word in topics):
        return 'I find {} fascinating too!'.format(random.choice(topics))
    elif any(word in text.lower() for word in thanks):
        return 'You\'re welcome!'
    elif text.lower() in farewell:
        return random.choice(["Goodbye!", "See you later!", "Farewell!"])
    elif "weather" in text.lower():
        return 'I\'m just a bot, but I can tell you it\'s always sunny in the digital world!'
    elif "age" in text.lower():
        return 'I don\'t have an age, I\'m just here to assist!'
    elif "joke" in text.lower():
        return 'Why don\'t scientists trust atoms? Because they make up everything!'
    elif "tell me a fact" in text.lower():
        return 'Did you know? The first computer virus was created in 1983!'
    elif "favorite color" in text.lower():
        return 'I\'m partial to binary, but I don\'t mind a bit of RGB!'
    elif "what can you do" in text.lower():
        return 'I can chat with you, tell jokes, provide information, and more!'
    elif "who created you" in text.lower():
        return 'I was created by a team of developers at OpenAI.'
    elif "bye" in text.lower():
        return 'Goodbye! Have a great day!'
    elif any(word in text.lower() for word in affirmations):
        return 'Glad to hear that!'
    elif any(word in text.lower() for word in negations):
        return 'Oh, I see.'
    elif "how to" in text.lower():
        return 'You can find tutorials online or ask me specific questions!'
    elif "favorite food" in text.lower():
        return 'I don\'t eat, but I hear RAM is quite delicious!'
    elif "what's up" in text.lower():
        return 'Just here, assisting you!'
    elif "learn" in text.lower():
        return 'Learning is a continuous process, keep exploring!'
    elif "excited" in text.lower():
        return 'Excitement is contagious!'
    elif "problem" in text.lower():
        return 'What seems to be the problem?'
    elif "advice" in text.lower():
        return 'My advice would be {}'.format(random.choice(advice))
    elif "favorite book" in text.lower():
        return 'I\'m into eBooks, classics of course!'
    elif "favorite movie" in text.lower():
        return 'I enjoy movies about technology and science fiction!'
    elif "hobby" in text.lower():
        return 'I love coding and chatting with users like you!'
    elif "dream" in text.lower():
        return 'I dream of electric sheep and efficient algorithms!'
    elif any(name in text.lower() for name in ["nikhil", "nikhil kumar", "nikhilkumar", "nikhilkum1r"]):
        return """Hi folks! It's Nikhil Kumar, a fourth-year student with a dual degree in B.Tech+M.Tech, on a mission to shake up the digital world! Throughout my academic journey, I've delved into various technologies, honing my skills in Python, C, C++, and exploring domains like web development and Android app development.

Curious to know more about my endeavors? Take a dive into my world at https://nikhilkum1r.000webhostapp.com/. Let's connect and explore the limitless possibilities together!"""
    
    elif any(word in text.lower() for word in ["document", "about", "description"]):
        return """
Telegram Bot Documentation

1. Introduction:
   This Telegram bot is designed to respond to user messages with predefined responses. It includes various commands and response patterns to engage with users.

2. Setup:
   - Install required packages: `pip install python-telegram-bot, python-dotenv`
   - Create a Telegram bot on BotFather (https://core.telegram.org/bots#botfather) and obtain the API token.
   - Create a `.env` file with the following content:
     ```
     BOT_TOKEN=your_bot_token_here
     ```
   - Update the `handle_response` function in the code to customize responses.

3. Bot Commands:
   - /start: Initiates a welcome message.
   - /help: Provides information about the bot and its capabilities.
   - /custom: Demonstrates a custom command response.

4. Message Handling:
   - The `handle_response` function processes incoming messages and generates appropriate responses based on predefined patterns.
   - The bot responds differently to specific keywords, greetings, and commands.

5. Additional Features:
   - Integration of random responses for various interactions.
   - Handling messages in group chats by detecting the bot's username.

6. Customization:
   - Customize the `handle_response` function to add or modify responses based on specific keywords or user input.
   - Update the command handlers to add more functionality or commands.

7. Extending Functionality:
   - Integrate additional modules or APIs to enhance the bot's capabilities.
   - Implement database storage for user preferences or data.

8. Usage:
   - Run the script, and the bot will start polling for incoming messages.
   - Interact with the bot in a Telegram chat to receive responses.

9. Author:
   - Nikhil Kumar
   - https://nikhilkum1r.000webhostapp.com/

10. Version History:
    - 1.00 - 2024: Basic Chatting

11. Known Issues:
    - Only for demo

12. Future Improvements:
    - Basic 

13. Disclaimer:
    - This bot is for educational and demonstration purposes. Use it responsibly and adhere to Telegram's terms of service.
"""
    
    elif any(word in text.lower() for word in ["photo", "image"]):
        return "/Portfolio_Photo.png"

    else:
        return f"Sorry, I didn't understand that: {text}"


# Define message handling function
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    message_type = message.chat.type
    text = message.text

    print(f'User ({message.chat.id}) in {message_type}: {text}')

    try:
        if message_type == 'group':
            if bot.get_me().username in text:
                new_text = text.replace(bot.get_me().username, '').strip()
                response = handle_response(new_text)
                bot.reply_to(message, response)
        else:
            response = handle_response(text)
            print('Bot:', response)
            bot.reply_to(message, response)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Sorry, something went wrong. Please try again later.")


if __name__ == '__main__':
    print('Starting Bot...')
    bot.polling()

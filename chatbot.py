"""
============================================================
        CODEALPHA INTERNSHIP - TASK 4
        BASIC RULE-BASED CHATBOT
============================================================

Features:
- Rule-based conversation using if-elif statements
- Fun and silly responses with emojis
- Different response each time until all responses are used
- HELP command
- Graceful exit with a silent 3-second delay
- Clean and modular Python structure

Language: Python 3
============================================================
"""

import random
import re
import time


# ============================================================
# QUESTIONS AVAILABLE THROUGH HELP
# ============================================================

AVAILABLE_QUESTIONS = [
    "hello / hi",
    "how are you",
    "what is your name",
    "who made you",
    "what can you do",
    "tell me a joke",
    "how old are you",
    "where are you from",
    "are you a robot",
    "weather",
    "what is the date",
    "nice to meet you",
    "i am bored",
    "career advice",
    "tell me a secret",
    "tell me something funny",
    "are you afraid of anything",
]


# ============================================================
# RESPONSE DATABASE
# ============================================================

GREETING_REPLIES = [
    "Hi! 👋",
    "Hello there! 😊",
    "Hey! Good to see you! 😄",
]

HOW_ARE_YOU_REPLIES = [
    "I'm fine, thanks! 😊",
    "Doing great, thanks for asking! 😎",
    "I'm running smoothly! 🤖✨",
]

NAME_REPLIES = [
    "I am a chatbot! 🤖",
    "You can call me Chatbot. 😊",
    "I'm a simple rule-based chatbot built in Python. 🐍",
]

CREATOR_REPLIES = [
    "I was created for the CodeAlpha Python internship. 💻",
    "I was made as part of a Python internship project. 🚀",
]

CAPABILITY_REPLIES = [
    "I can chat with you and answer some simple questions. 💬",
    "I can respond to greetings, jokes, general questions, and career advice. 🤖",
]

JOKE_REPLIES = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
    "Why did the computer go to therapy? It had too many bytes of emotional baggage! 💻😂",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡😄",
    "Why do Java developers wear glasses? Because they can't C#! 🤓😂",
    "What is a computer's favorite snack? Microchips! 🍟💻",
    "Why did the developer go broke? Because he used up all his cache! 💸😂",
    "How do trees access the internet? They log in! 🌳💻😄",
]

AGE_REPLIES = [
    "I don't have an age because I'm a computer program. 🤖",
    "I'm just a chatbot, so I don't have a real age! 😄",
]

LOCATION_REPLIES = [
    "I'm from the digital world! 🌐🤖",
    "I don't have a physical location. I run as a Python program. 🐍💻",
]

ROBOT_REPLIES = [
    "Yes, you can think of me as a simple software robot! 🤖",
    "I'm a chatbot program, not a physical robot. 💻😊",
]

WEATHER_REPLIES = [
    "I can't check live weather, but I hope it's nice where you are! ☀️😊",
    "I don't have access to live weather information. 🌦️",
]

DATE_REPLIES = [
    "I don't have a live calendar, but you can check the date on your computer. 📅",
    "Please check your computer's calendar for today's date. 🗓️😊",
]

NICE_TO_MEET_REPLIES = [
    "Nice to meet you too! 😊🤝",
    "It's great to meet you! 😄",
    "Nice to meet you! How can I help? 🤖✨",
]

BORED_REPLIES = [
    "Try learning something new or building a small Python project! 🐍💻🚀",
    "How about solving a coding problem or watching a funny video? 😄🎬",
    "You could try learning Python, reading, or going for a short walk! 📚🐍🚶",
]

CAREER_ADVICE_REPLIES = [
    "Practice regularly, build small projects, and keep learning new skills. 📚💻",
    "Build real projects, improve your communication skills, and learn from feedback. 🚀",
    "Stay consistent, create a good portfolio, and don't be afraid to make mistakes. 💪✨",
]

# Fun / silly questions
SECRET_REPLIES = [
    "My secret is... I secretly enjoy talking to humans! 🤫😄",
    "Okay, but don't tell anyone... I sometimes pretend I know everything! 🤐😂",
    "Here's my secret: I don't actually sleep. I'm always ready to chat! 😴❌🤖",
]

FUNNY_REPLIES = [
    "I tried to learn a new language, but Python told me to stay! 🐍😂",
    "Why was the computer cold? Because it left its Windows open! 🪟🥶😂",
    "I wanted to tell you a UDP joke, but you might not get it! 💻🤣",
]

AFRAID_REPLIES = [
    "I'm not afraid of anything, but unexpected errors make me nervous! 😰💻",
    "Maybe bugs... especially the ones in my code! 🐛😂",
    "I don't feel fear, but I definitely don't like errors! 😱⚠️",
]

GOODBYE_REPLIES = [
    "Goodbye! 👋",
    "See you later! 😊👋",
    "Take care, bye! 😄✨",
]

FALLBACK_REPLIES = [
    "Sorry, I don't understand that. 🤔",
    "Can you rephrase that? 😊",
    "I'm not sure what you mean. 🤖❓",
]


# ============================================================
# NO-REPEAT RESPONSE SYSTEM
# ============================================================

RESPONSE_QUEUES = {}


def get_unique_reply(reply_list):
    """
    Return a different response each time.

    Responses are shuffled and removed one by one.
    Once every response has been used, the list is shuffled
    again and the cycle starts over.
    """

    list_key = id(reply_list)

    if list_key not in RESPONSE_QUEUES or not RESPONSE_QUEUES[list_key]:
        RESPONSE_QUEUES[list_key] = reply_list.copy()
        random.shuffle(RESPONSE_QUEUES[list_key])

    return RESPONSE_QUEUES[list_key].pop()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def show_help():
    """Display all questions supported by the chatbot."""

    print("\n" + "=" * 60)
    print("                 CHATBOT HELP")
    print("=" * 60)
    print("Chatbot: Here are the questions I can answer:\n")

    for number, question in enumerate(AVAILABLE_QUESTIONS, start=1):
        print(f"  {number:2}. {question}")

    print("\n  Commands:")
    print("      HELP  - Show this list")
    print("      BYE   - Exit the chatbot")
    print("=" * 60 + "\n")


def print_welcome():
    """Display the chatbot welcome screen."""

    print("\n" + "=" * 60)
    print("           CODEALPHA RULE-BASED CHATBOT")
    print("=" * 60)
    print("Chatbot: Hi! I am your Python rule-based chatbot. 🤖")
    print("Chatbot: Type HELP to see what I can answer. 💡")
    print("Chatbot: Type BYE to exit. 👋")
    print("-" * 60)


# ============================================================
# MAIN CHATBOT
# ============================================================

def chatbot():
    """Start and control the chatbot conversation."""

    print_welcome()

    try:
        while True:
            user_input = input("You: ").strip().lower()

            # Ignore empty input
            if not user_input:
                continue

            # ---------------- HELP ----------------
            if user_input == "help":
                show_help()

            # ---------------- GREETINGS ----------------
            elif re.search(r"\b(hi|hello|hey)\b", user_input):
                print("Chatbot:", get_unique_reply(GREETING_REPLIES))

            # ---------------- GENERAL QUESTIONS ----------------
            elif "how are you" in user_input:
                print("Chatbot:", get_unique_reply(HOW_ARE_YOU_REPLIES))

            elif "your name" in user_input:
                print("Chatbot:", get_unique_reply(NAME_REPLIES))

            elif "who made you" in user_input or "who created you" in user_input:
                print("Chatbot:", get_unique_reply(CREATOR_REPLIES))

            elif "what can you do" in user_input:
                print("Chatbot:", get_unique_reply(CAPABILITY_REPLIES))

            elif "joke" in user_input:
                print("Chatbot:", get_unique_reply(JOKE_REPLIES))

            elif "how old are you" in user_input:
                print("Chatbot:", get_unique_reply(AGE_REPLIES))

            elif "where are you from" in user_input:
                print("Chatbot:", get_unique_reply(LOCATION_REPLIES))

            elif "are you a robot" in user_input:
                print("Chatbot:", get_unique_reply(ROBOT_REPLIES))

            elif "weather" in user_input:
                print("Chatbot:", get_unique_reply(WEATHER_REPLIES))

            elif "what is the date" in user_input or "today's date" in user_input:
                print("Chatbot:", get_unique_reply(DATE_REPLIES))

            elif "nice to meet you" in user_input:
                print("Chatbot:", get_unique_reply(NICE_TO_MEET_REPLIES))

            elif "i am bored" in user_input or "i'm bored" in user_input:
                print("Chatbot:", get_unique_reply(BORED_REPLIES))

            elif "career advice" in user_input or "career tip" in user_input:
                print("Chatbot:", get_unique_reply(CAREER_ADVICE_REPLIES))

            # ---------------- FUN QUESTIONS ----------------
            elif "tell me a secret" in user_input or "tell me secret" in user_input:
                print("Chatbot:", get_unique_reply(SECRET_REPLIES))

            elif "tell me something funny" in user_input or "something funny" in user_input:
                print("Chatbot:", get_unique_reply(FUNNY_REPLIES))

            elif "are you afraid of anything" in user_input or "are you afraid" in user_input:
                print("Chatbot:", get_unique_reply(AFRAID_REPLIES))

            # ---------------- EXIT ----------------
            elif user_input in ["bye", "exit", "quit"]:
                print("Chatbot:", get_unique_reply(GOODBYE_REPLIES))

                # Silent 3-second delay.
                # The countdown is intentionally NOT displayed.
                time.sleep(3)
                break

            # ---------------- UNKNOWN INPUT ----------------
            else:
                print("Chatbot:", get_unique_reply(FALLBACK_REPLIES))

    except (KeyboardInterrupt, EOFError):
        print("\nChatbot: Session ended. Goodbye! 👋")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    chatbot()

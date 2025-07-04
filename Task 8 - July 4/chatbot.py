import random
import sys
import time
from datetime import datetime

# Typewriter effect with spacing
def type_print(message, delay=0.03):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")  # Adds a one-line space after each response


# Data
greetings = ["Hello!", "Hi there!", "Hey!", "Hi!"]
goodbyes = ["Goodbye!", "See ya!", "Take care!", "Bye!"]
jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "Why don’t scientists trust atoms? Because they make up everything!",
]
facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!",
    "Bananas are berries, but strawberries aren't!",
    "Octopuses have three hearts!",
    "The Eiffel Tower can grow more than 6 inches during hot days.",
    "A group of flamingos is called a flamboyance.",
]

type_print(
    "🤖 PyBot: Hello! I'm your simple chatbot. Type 'exit' to end the conversation."
)

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["exit", "bye", "quit"]:
        type_print("PyBot: " + random.choice(goodbyes))
        break

    elif any(greet in user_input for greet in ["hi", "hello", "hey"]):
        type_print("PyBot: " + random.choice(greetings))

    elif "how are you" in user_input:
        type_print("PyBot: I'm doing well, thanks for asking! 😊, How can I help you today?")

    elif any(
        feeling in user_input
        for feeling in [
            "i'm good",
            "i am good",
            "i'm fine",
            "i am fine",
            "i'm okay",
            "i am okay",
            "i'm great",
            "i am great",
        ]
    ):
        type_print("PyBot: Glad to hear that! 😄 How can I assist you today?")

    elif any(
        feeling in user_input
        for feeling in [
            "i'm sad",
            "i am sad",
            "not good",
            "not okay",
            "bad",
            "terrible",
            "upset",
        ]
    ):
        type_print(
            "PyBot: I'm sorry to hear that. 😔 Want to talk about it or hear a joke to cheer you up?"
        )

    elif "python" in user_input:
        type_print(
            "PyBot: Python is a high-level, versatile programming language. Great choice!"
        )

    elif "who made you" in user_input or "creator" in user_input:
        type_print(
            "PyBot: I was created by a Python Developer Intern — that's confidential! 😉"
        )

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        type_print(f"PyBot: The current time is {current_time}")

    elif "date" in user_input:
        today = datetime.now().strftime("%Y-%m-%d")
        type_print(f"PyBot: Today's date is {today}")

    elif "joke" in user_input:
        type_print("PyBot: " + random.choice(jokes))

    elif "weather" in user_input:
        type_print(
            "PyBot: I'm not connected to weather APIs yet, but it's probably fine out there!"
        )

    elif "fact" in user_input or "surprise" in user_input:
        type_print("PyBot: Here's a fun fact for you!")
        type_print("👉 " + random.choice(facts))

    elif "game" in user_input:
        type_print(
            "PyBot: Let's play a guessing game! I'm thinking of a number between 1 and 5."
        )
        number = random.randint(1, 5)
        try:
            guess = int(input("Your guess: "))
            if guess == number:
                type_print("PyBot: 🎉 You're right!")
            else:
                type_print(f"PyBot: Nope! It was {number}. Better luck next time.")
        except ValueError:
            type_print("PyBot: That doesn't look like a number.")

    elif "calculate" in user_input or "solve" in user_input:
        type_print("PyBot: Type a math expression like 2 + 3 or 5 * 6")
        expression = input("🧮 Expression: ")
        try:
            result = eval(expression)
            type_print(f"PyBot: The answer is {result}")
        except:
            type_print("PyBot: That doesn't look like a valid math expression.")

    elif "sad" in user_input or "unhappy" in user_input:
        type_print("PyBot: Hey, Do not worry!, I'm here for you ❤️.")

    elif "happy" in user_input or "excited" in user_input:
        type_print("PyBot: Yay! That makes me happy too 😄")

    elif "help" in user_input or "menu" in user_input:
        type_print("PyBot: Here's what I can do:")
        type_print(
            "- Tell jokes\n- Share fun facts\n- Tell time/date\n- Solve math\n- Play a game\n- Greet you\n- Say goodbye"
        )

    else:
        type_print("PyBot: Sorry, I didn't understand that. Can you rephrase?")

# PyBot: Rule-Based Chatbot CLI Application
A simple command-line chatbot built in Python using condition-based rules. PyBot simulates conversational interaction with users using keyword detection and predefined responses. It includes a typing effect for realistic feel and supports fun features like telling jokes, sharing facts, solving math problems, and playing a mini game.

## Features
- Typewriter Output: Each bot response is displayed with animated character-by-character typing.
- Keyword Detection: Uses `if-elif` conditions to simulate natural responses based on intent.
- Joke & Fact Generator: Shares random jokes and surprising facts.
- Time & Date Info: Tells the current system time and date.
- Mood Detection: Responds differently to happy, sad, or neutral messages.
- Math Solver: Evaluates simple math expressions given by the user.
- Number Guessing Game: A fun mini-game for quick interaction.
- Help/Menu: Lists supported commands and features.
- No External Libraries: Pure Python (standard library only).


## Implementation Overview
- Typewriter Effect: Uses `sys.stdout.write()` and `time.sleep()` to simulate typing.
- Input Loop: Continuously waits for user input until "exit", "bye", or "quit" is received.
- Greetings & Farewells: Responds to "hi", "hello", "bye", etc., with randomized responses.
- Condition Matching: Uses `in` keyword to detect intent in lowercase user input.
- Randomized Replies: Jokes, facts, greetings, and goodbyes are selected randomly from lists.
- Exception Handling: Catches invalid input (like letters in number guessing or math).
- Personalization (Planned): Easily extensible to support user memory, name saving, etc.

## Execution
```
🤖 PyBot: Hello! I'm your simple chatbot. Type 'exit' to end the conversation. 

You: hi
PyBot: Hey!

You: how are you?
PyBot: I'm doing well, thanks for asking! 😊, How can I help you today?

You: tell me a joke
PyBot: Why don’t scientists trust atoms? Because they make up everything!

You: surprise me
PyBot: Here's a fun fact for you!

👉 The Eiffel Tower can grow more than 6 inches during hot days.

You: what's the time ?
PyBot: The current time is 11:45:00

You: and the date ?
PyBot: Today's date is 2025-07-04

You: calculate
PyBot: Type a math expression like 2 + 3 or 5 * 6

🧮 Expression: 32*52
PyBot: The answer is 1664

You: play a game
PyBot: Let's play a guessing game! I'm thinking of a number between 1 and 5.

Your guess: 4
PyBot: Nope! It was 2. Better luck next time.

You: i am feeling sad
PyBot: Hey, Do not worry!, I'm here for you ❤️.

You: need a help
PyBot: Here's what I can do:

- Tell jokes
- Share fun facts
- Tell time/date
- Solve math
- Play a game
- Greet you
- Say goodbye

You: solve math
PyBot: Type a math expression like 2 + 3 or 5 * 6

🧮 Expression: 23+23*4
PyBot: The answer is 115

You: bye
PyBot: Goodbye!

PS D:\Elevate Labs - Python Development> 
```

## Getting started
1. Clone this repository to your local machine.

   ```
   https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git
   ```

   ```
   cd 'Task 8 - July 4'
   ```

2. Run the chatbot script.
   Make sure you have Python installed (version 3.6+ recommended).

   ```
   python chatbot.py
   ```

## Acknowledgments
This chatbot was developed as part of the Python Developer Internship at Elevate Labs. It demonstrates basic rule-based NLP structure, control flow, input handling, and user interaction in a beginner-friendly console environment.

## License
This project is released under the MIT License. Feel free to use and learn!

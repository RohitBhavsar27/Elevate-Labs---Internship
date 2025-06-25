# Console To-Do List CLI Application
A simple command-line interface (CLI), persistent To-Do List manager built in Python that allows you to store tasks in a local text file, so your list survives across sessions without the need for a graphical user interface.

## Features
- Persistent Storage: Tasks survive restarts by reading/writing tasks.txt.
- Intuitive CLI: Clear menu and prompts guide user through operations.
- Error Handling: Catches bad inputs and missing files without crashing.
- Dynamic Formatting: Automatically formats task list into a neat table.
- Zero Dependencies: Pure Python standard-library implementation—no installs needed.


## Implementation Overview
- Initialization: Load tasks.txt into a Python list or start empty if file missing.
- Menu Display: Show numbered options—Add, View, Mark Done, Exit—in a loop.
- Add Task: Prompt for description, validate non-empty, append to list, save to file.
- View Tasks: Render all tasks as a two-column table with serial numbers.
- Mark as Done: Ask for task number, validate index, remove from list, update file.
- Persistence: Rewrite tasks.txt on every change to keep data across sessions.
- Exit: Break loop and end program with a goodbye message.

## Execution
![Screenshot 2025-06-25 171144](https://github.com/user-attachments/assets/1a6c866e-9b46-45b3-bbac-6caf0c50ae48)

![Screenshot 2025-06-25 171231](https://github.com/user-attachments/assets/7ad7f37c-09e7-47ce-b5db-5f6ef9c65220)

![Screenshot 2025-06-25 171314](https://github.com/user-attachments/assets/655ea720-2b2b-4922-9f8c-c32a381de293)

## Getting started
1. Clone this repository to your local machine.

   ```https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git```

   ```cd Task 2 - June 25```

3. Run the todo list CLI.
   Make sure you have Python installed (version 3.6+ recommended).

   ```python todo_list.py```

## Acknowledgments
This To-Do List CLI application was inspired by the need for a lightweight and command-line based To-Do List for quickly storing tasks that survives accross various sessions.

## License
This project is released under the MIT License. Feel free to use and learn!


TASKS_FILE = "Task 2 - June 25\\tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def display_menu():
    print("\nSelect Operation")
    print("\n1. Add Task\n2. View Task\n3. Mark as done\n4. Exit")


def add_task(tasks):
    task = input("Enter task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if tasks:
        # print("-" * 50)
        print("|{:^10}|{:^37}|".format("Sr.No", "Tasks"))
        print("-" * 50)
        for i, task in enumerate(tasks, 1):
            print("|{:^10}|{:^37}|".format(i, task))
        print("-" * 50)
    else:
        print("No tasks available.")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' marked as done and removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    print("-" * 50)
    print(f"Simple To-Do List Application - Powered by Python")
    print("-" * 50)

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            print("-" * 50)

            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                print("Exiting. Have a productive day!")
                break
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

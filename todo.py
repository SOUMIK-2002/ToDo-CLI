# File name where tasks will be saved
FILENAME = "tasks.txt"

# Load tasks from the file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    print("\n--- TO-DO LIST ---")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a new task
def add_task(tasks):
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print("Task added successfully.")
    else:
        print("Empty task not added.")

# Remove a task by number
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Show menu
def show_menu():
    print("\nChoose an option:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main application loop
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

# Run the app
if __name__ == "__main__":
    main()
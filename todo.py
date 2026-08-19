# To-Do List Application

tasks = []


def display_menu():
    """Display the main menu options."""
    print("\n--- TO-DO LIST APP ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")


def add_task(tasks):
    """Add a non-empty task to the task list."""
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        print(f'"{task}" was added to your list.')
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    """Display all tasks, or an empty-list message."""
    if not tasks:
        print("There are no tasks to view.")
    else:
        print("\n--- YOUR TASKS ---")

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def delete_task(tasks):
    """Delete a task selected by its displayed number."""
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the number of the task to delete: "))

        task_index = task_number - 1

        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f'"{deleted_task}" was removed from your list.')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid whole number.")

    else:
        print("Delete operation completed.")

    finally:
        print("Returning to the main menu.")


def main():
    """Run the To-Do List Application."""
    print("Welcome to the To-Do List App!")

    while True:
        display_menu()

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Thanks for using the To-Do List App. Goodbye!")
            break

        else:
            print("Invalid menu option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
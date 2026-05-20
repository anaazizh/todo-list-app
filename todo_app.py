"""
todo_app.py
-----------
SE Foundations: To-Do List Application

A beginner-friendly command-line to-do list manager.
Tasks are stored in a Python list that lives in memory for the
duration of the program session.

Author : Ana Aziz Hemani
Course : SE Foundations
"""


# ---------------------------------------------------------------------------
# Data storage
# ---------------------------------------------------------------------------

tasks = []  # All to-do items are kept in this list as plain strings.


# ---------------------------------------------------------------------------
# Helper / display functions
# ---------------------------------------------------------------------------

def display_welcome():
    """Print a welcome banner when the program starts."""
    print("=" * 40)
    print("   Welcome to the To-Do List App!")
    print("=" * 40)
    print("Manage your tasks right from the terminal.\n")


def display_menu():
    """Print the main menu options to the screen."""
    print("\n--- Main Menu ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Quit")
    print("-" * 17)


# ---------------------------------------------------------------------------
# Core feature functions
# ---------------------------------------------------------------------------

def add_task():
    """
    Prompt the user for a task description and add it to the tasks list.

    Uses a try/except/else/finally block to handle unexpected errors
    while collecting input.
    """
    try:
        new_task = input("Enter the task you want to add: ").strip()

        # An empty string is not a valid task.
        if not new_task:
            raise ValueError("Task description cannot be empty.")

    except ValueError as error:
        # Let the user know what went wrong.
        print(f"  [Error] {error}")

    else:
        # This block runs only when no exception was raised above.
        tasks.append(new_task)
        print(f"  Task added: \"{new_task}\"")

    finally:
        # This block always runs, whether or not an error occurred.
        print("  (add_task finished)")


def view_tasks():
    """
    Display all tasks currently stored in the tasks list.

    Alerts the user if the list is empty so they know there is
    nothing to show yet.

    Uses a try/except/else/finally block for safe execution.
    """
    try:
        # Check for an empty list before trying to display anything.
        if not tasks:
            raise IndexError("There are no tasks to display.")

    except IndexError as error:
        print(f"  [Alert] {error}")

    else:
        # Only reached when at least one task exists.
        print("\n  Your To-Do List:")
        print("  " + "-" * 20)
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")
        print("  " + "-" * 20)

    finally:
        print("  (view_tasks finished)")


def delete_task():
    """
    Prompt the user for a task number and remove it from the tasks list.

    Handles three distinct error cases:
      - No tasks exist yet (nothing to delete).
      - User types something that is not a whole number.
      - The number entered is outside the valid range.

    Uses a try/except/else/finally block to manage all error paths.
    """
    try:
        # Guard: nothing to delete if the list is empty.
        if not tasks:
            raise ValueError("There are no tasks to delete.")

        # Show the current list so the user knows which number to pick.
        view_tasks()

        raw_input = input("  Enter the task number to delete: ").strip()

        # Convert to integer – raises ValueError if input is not numeric.
        task_number = int(raw_input)

        # Check that the number is within the bounds of the list.
        if task_number < 1 or task_number > len(tasks):
            raise IndexError(
                f"Task number {task_number} does not exist. "
                f"Please choose a number between 1 and {len(tasks)}."
            )

    except ValueError as error:
        print(f"  [Error] {error}")

    except IndexError as error:
        print(f"  [Error] {error}")

    else:
        # Runs only when no exception occurred above.
        # Lists are 0-indexed, so subtract 1 from the displayed number.
        removed = tasks.pop(task_number - 1)
        print(f"  Task deleted: \"{removed}\"")

    finally:
        print("  (delete_task finished)")


# ---------------------------------------------------------------------------
# Menu dispatcher
# ---------------------------------------------------------------------------

def handle_menu_choice(choice):
    """
    Call the appropriate function based on the user's menu selection.

    Parameters
    ----------
    choice : str
        The raw string typed by the user at the menu prompt.

    Uses a try/except/else/finally block so that an unrecognised option
    is reported clearly without crashing the program.
    """
    try:
        # Only accept the four valid options.
        if choice not in ("1", "2", "3", "4"):
            raise ValueError(
                f"\"{choice}\" is not a valid menu option. "
                "Please enter 1, 2, 3, or 4."
            )

    except ValueError as error:
        print(f"  [Alert] {error}")

    else:
        # Route to the correct feature function.
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        # choice == "4" (Quit) is handled in the main loop.

    finally:
        print("  (handle_menu_choice finished)")


# ---------------------------------------------------------------------------
# Main program loop
# ---------------------------------------------------------------------------

def main():
    """
    Entry point for the To-Do List Application.

    Displays the welcome message and then repeatedly shows the menu
    until the user selects option 4 (Quit).
    """
    display_welcome()

    while True:
        display_menu()

        # Collect the user's menu selection.
        user_choice = input("Enter your choice (1-4): ").strip()

        # Check for quit before calling handle_menu_choice so we exit cleanly.
        if user_choice == "4":
            print("\nThank you for using the To-Do List App. Goodbye!")
            break

        handle_menu_choice(user_choice)


# ---------------------------------------------------------------------------
# Program entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()

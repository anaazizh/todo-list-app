# SE Foundations – To-Do List Application

## Overview

This is a beginner-friendly command-line To-Do List application written in Python.
It lets you add, view, and delete tasks within a single session.
All tasks are stored in a Python list — no databases or files are involved —
so the list starts fresh each time you run the program.

---

## Features

| Feature | Description |
|---|---|
| **Welcome screen** | A greeting banner is printed when the program starts. |
| **Interactive menu** | Four clearly labelled options: Add, View, Delete, Quit. |
| **Add a task** | Type any text to create a new task. Empty input is rejected. |
| **View all tasks** | Numbered list of current tasks, or an alert if nothing exists yet. |
| **Delete a task** | Remove a task by number; alerts on empty list or bad number. |
| **Quit** | Exits the program with a farewell message. |
| **Input validation** | Invalid menu options are caught and reported without crashing. |
| **Error handling** | Every feature uses `try`, `except`, `else`, and `finally` blocks. |

---

## Requirements

- **Python 3.6 or newer** (no third-party packages needed)

Check your Python version:

```
python --version
```

or, on some systems:

```
python3 --version
```

---

## How to Run

### In VS Code

1. Open VS Code and choose **File → Open Folder**, then select the `todo_application` folder.
2. Open the **Explorer** panel (left sidebar) and click `todo_app.py`.
3. Open the integrated terminal: **Terminal → New Terminal** (or `` Ctrl+` ``).
4. In the terminal, run:

```
python todo_app.py
```

> On macOS/Linux you may need `python3 todo_app.py`.

### In a Regular Terminal

1. Navigate to the project folder:

```
cd path/to/todo_application
```

2. Run the script:

```
python todo_app.py
```

---

## Usage Flow

```
========================================
   Welcome to the To-Do List App!
========================================
Manage your tasks right from the terminal.

--- Main Menu ---
1. Add a task
2. View all tasks
3. Delete a task
4. Quit
-----------------
Enter your choice (1-4): 1
Enter the task you want to add: Buy groceries
  Task added: "Buy groceries"
  (add_task finished)
  (handle_menu_choice finished)

--- Main Menu ---
...
Enter your choice (1-4): 2
  Your To-Do List:
  --------------------
  1. Buy groceries
  --------------------
  (view_tasks finished)
  (handle_menu_choice finished)

--- Main Menu ---
...
Enter your choice (1-4): 3
  (view_tasks output shown)
  Enter the task number to delete: 1
  Task deleted: "Buy groceries"
  (delete_task finished)
  (handle_menu_choice finished)

--- Main Menu ---
...
Enter your choice (1-4): 4

Thank you for using the To-Do List App. Goodbye!
```

---

## Testing Checklist

Work through each item below and confirm the expected result before submitting.

### Normal operations
- [ ] Run the program – the welcome banner appears.
- [ ] Select **1** – add a task with a normal description (e.g. "Walk the dog").
- [ ] Select **2** – the task appears in a numbered list.
- [ ] Select **1** again – add a second task.
- [ ] Select **2** – both tasks are shown with correct numbers.
- [ ] Select **3** – delete task number 1; confirm it is removed.
- [ ] Select **2** – only the remaining task is shown.
- [ ] Select **4** – the program exits with "Goodbye!".

### Edge cases / error handling
- [ ] Select **2** on an empty list → alert: "There are no tasks to display."
- [ ] Select **3** on an empty list → alert: "There are no tasks to delete."
- [ ] Select **1** and press Enter without typing anything → alert: "Task description cannot be empty."
- [ ] Select **3**, then enter a number larger than the list length → alert about nonexistent task number.
- [ ] Select **3**, then enter `0` or a negative number → alert about nonexistent task number.
- [ ] Select **3**, then enter letters (e.g. `abc`) → alert about invalid input.
- [ ] At the main menu, type an invalid option (e.g. `9` or `hello`) → alert: "is not a valid menu option."

### Code review
- [ ] Every function has a docstring.
- [ ] Each feature function contains `try`, `except`, `else`, and `finally` blocks.
- [ ] Tasks are stored in a plain Python `list`.
- [ ] `input()` is used for all user interaction.
- [ ] No external libraries are imported.

---

## Project Structure

```
todo_application/
├── todo_app.py        # Main application source code
├── README.md          # Project information and usage instructions
└── test_todo_app.py   # Optional automated test script
```

---

## Submission Reminder

Before you submit:

1. Confirm **all checklist items** above are ticked.
2. Re-read your code and add or improve any comments that are unclear.
3. Double-check that you have **not** imported any external libraries in `todo_app.py`.
4. Create a GitHub repository, then add, commit, and push these files.
5. Submit your GitHub repository URL in Disco.
6. Record and upload your video directly to Disco. Do **not** use Google Drive or an external video link.

## Suggested Video Outline

Keep the video under 5 minutes and make sure your face is visible on camera.

1. **What the project does** — Explain that this is a command-line To-Do List app where users can add, view, delete, and quit.
2. **How it works** — Mention that tasks are stored in a Python list and that the program uses functions, loops, conditionals, input validation, and `try`/`except`/`else`/`finally` blocks.
3. **Quick demo** — Run `python todo_app.py`, add one or two tasks, view them, delete one task, show an invalid input example, and quit.

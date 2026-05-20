"""
test_todo_app.py
----------------
Automated tests for todo_app.py.

Each test pipes a sequence of simulated keystrokes into the app via stdin
and checks that expected output strings appear in the captured output.

Run with:  python test_todo_app.py
"""

import subprocess
import sys

PYTHON = sys.executable
APP = "todo_app.py"

PASS = "[PASS]"
FAIL = "[FAIL]"

results = []


def run_app(inputs: list[str]) -> str:
    """
    Launch todo_app.py as a subprocess, feed it the given list of input
    lines, and return the combined stdout output as a single string.
    """
    stdin_data = "\n".join(inputs) + "\n"
    proc = subprocess.run(
        [PYTHON, APP],
        input=stdin_data,
        capture_output=True,
        text=True,
        cwd="/home/user/workspace/todo_application",
    )
    return proc.stdout + proc.stderr  # merge so we see everything


def check(test_name: str, output: str, expected_phrases: list[str]):
    """
    Verify that every phrase in expected_phrases appears somewhere in output.
    Print pass/fail and record the result.
    """
    all_ok = True
    missing = []
    for phrase in expected_phrases:
        if phrase not in output:
            all_ok = False
            missing.append(phrase)

    status = PASS if all_ok else FAIL
    results.append((status, test_name))
    print(f"{status}  {test_name}")
    if missing:
        for m in missing:
            print(f"       Missing: {repr(m)}")
        print("       --- captured output ---")
        for line in output.splitlines():
            print(f"       | {line}")
        print("       ------------------------")


# ---------------------------------------------------------------------------
# Test 1 – Welcome message and menu appear on startup
# ---------------------------------------------------------------------------
out = run_app(["4"])
check(
    "Welcome banner and menu displayed",
    out,
    ["Welcome to the To-Do List App!", "Main Menu", "1. Add a task", "4. Quit"],
)

# ---------------------------------------------------------------------------
# Test 2 – Add a single task and view it
# ---------------------------------------------------------------------------
out = run_app(["1", "Buy groceries", "2", "4"])
check(
    "Add task and view it",
    out,
    ['Task added: "Buy groceries"', "1. Buy groceries"],
)

# ---------------------------------------------------------------------------
# Test 3 – Add multiple tasks and view all
# ---------------------------------------------------------------------------
out = run_app(["1", "Task A", "1", "Task B", "1", "Task C", "2", "4"])
check(
    "Add multiple tasks – all appear in numbered list",
    out,
    ["1. Task A", "2. Task B", "3. Task C"],
)

# ---------------------------------------------------------------------------
# Test 4 – View on empty list shows alert
# ---------------------------------------------------------------------------
out = run_app(["2", "4"])
check(
    "View empty list – alert shown",
    out,
    ["There are no tasks to display."],
)

# ---------------------------------------------------------------------------
# Test 5 – Delete on empty list shows alert
# ---------------------------------------------------------------------------
out = run_app(["3", "4"])
check(
    "Delete on empty list – alert shown",
    out,
    ["There are no tasks to delete."],
)

# ---------------------------------------------------------------------------
# Test 6 – Add then delete a task
# ---------------------------------------------------------------------------
out = run_app(["1", "Mow the lawn", "3", "1", "2", "4"])
check(
    "Add then delete task – task removed, list empty alert shown",
    out,
    ['Task deleted: "Mow the lawn"', "There are no tasks to display."],
)

# ---------------------------------------------------------------------------
# Test 7 – Delete with out-of-range number (too high)
# ---------------------------------------------------------------------------
out = run_app(["1", "Only task", "3", "99", "4"])
check(
    "Delete out-of-range number – error shown",
    out,
    ["does not exist"],
)

# ---------------------------------------------------------------------------
# Test 8 – Delete with zero (invalid index)
# ---------------------------------------------------------------------------
out = run_app(["1", "Task one", "3", "0", "4"])
check(
    "Delete task number 0 – error shown",
    out,
    ["does not exist"],
)

# ---------------------------------------------------------------------------
# Test 9 – Delete with non-numeric input
# ---------------------------------------------------------------------------
out = run_app(["1", "Some task", "3", "abc", "4"])
check(
    "Delete non-numeric input – ValueError shown",
    out,
    ["[Error]"],
)

# ---------------------------------------------------------------------------
# Test 10 – Add empty task (blank input)
# ---------------------------------------------------------------------------
out = run_app(["1", "", "4"])
check(
    "Add empty task – error shown",
    out,
    ["Task description cannot be empty."],
)

# ---------------------------------------------------------------------------
# Test 11 – Invalid menu choice (number out of range)
# ---------------------------------------------------------------------------
out = run_app(["9", "4"])
check(
    "Invalid menu option '9' – alert shown",
    out,
    ["is not a valid menu option"],
)

# ---------------------------------------------------------------------------
# Test 12 – Invalid menu choice (text)
# ---------------------------------------------------------------------------
out = run_app(["hello", "4"])
check(
    "Invalid menu option 'hello' – alert shown",
    out,
    ["is not a valid menu option"],
)

# ---------------------------------------------------------------------------
# Test 13 – Quit exits with farewell message
# ---------------------------------------------------------------------------
out = run_app(["4"])
check(
    "Quit – farewell message displayed",
    out,
    ["Thank you for using the To-Do List App. Goodbye!"],
)

# ---------------------------------------------------------------------------
# Test 14 – finally blocks run after successful add
# ---------------------------------------------------------------------------
out = run_app(["1", "Test task", "4"])
check(
    "finally block runs after successful add",
    out,
    ["(add_task finished)"],
)

# ---------------------------------------------------------------------------
# Test 15 – finally blocks run after an error (empty add)
# ---------------------------------------------------------------------------
out = run_app(["1", "", "4"])
check(
    "finally block runs even after error in add",
    out,
    ["(add_task finished)"],
)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
passed = sum(1 for s, _ in results if s == PASS)
failed = sum(1 for s, _ in results if s == FAIL)
total = len(results)

print()
print("=" * 40)
print(f"Results: {passed}/{total} passed, {failed} failed")
print("=" * 40)

if failed:
    sys.exit(1)

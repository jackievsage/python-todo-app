"""
todo.py — A simple command-line To-Do List app
Freshman CS Project | Covers: lists, dicts, file I/O, functions, loops
"""

import json
import os
from datetime import datetime

# ── File where tasks are saved ─────────────────────────────────────────────
DATA_FILE = "tasks.json"

PRIORITY_LABELS = {1: "🔴 High", 2: "🟡 Medium", 3: "🟢 Low"}
PRIORITY_ORDER  = {1: 0, 2: 1, 3: 2}   # for sorting


# ── Data helpers ───────────────────────────────────────────────────────────

def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if none exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# ── Display helpers ────────────────────────────────────────────────────────

def print_header():
    print("\n" + "=" * 45)
    print("         ✅  MY TO-DO LIST  ✅")
    print("=" * 45)


def print_tasks(tasks):
    """Print all tasks in a formatted table."""
    print_header()

    if not tasks:
        print("  (no tasks yet — add one below!)")
        print("=" * 45)
        return

    # Sort by priority, then by date added
    sorted_tasks = sorted(tasks, key=lambda t: (PRIORITY_ORDER[t["priority"]], t["added"]))

    for i, task in enumerate(sorted_tasks, start=1):
        status  = "✔" if task["done"] else "○"
        label   = PRIORITY_LABELS[task["priority"]]
        title   = task["title"]
        if task["done"]:
            title = f"\033[9m{title}\033[0m"   # strikethrough in most terminals
        print(f"  {i:>2}. [{status}] {title:<28} {label}")

    total = len(tasks)
    done  = sum(1 for t in tasks if t["done"])
    print("=" * 45)
    print(f"  Progress: {done}/{total} tasks complete")
    print("=" * 45)


# ── Core actions ───────────────────────────────────────────────────────────

def add_task(tasks):
    title = input("\n  Task title: ").strip()
    if not title:
        print("  ⚠  No title entered — task not added.")
        return

    print("  Priority:  1 = High  |  2 = Medium  |  3 = Low")
    choice = input("  Your choice [1/2/3]: ").strip()

    if choice not in ("1", "2", "3"):
        print("  ⚠  Invalid priority — defaulting to Medium.")
        choice = "2"

    task = {
        "title":    title,
        "priority": int(choice),
        "done":     False,
        "added":    datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"  ✅  Added: \"{title}\"")


def complete_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("\n  Mark task # as done (0 to cancel): "))
    except ValueError:
        print("  ⚠  Please enter a number.")
        return

    if num == 0:
        return

    sorted_tasks = sorted(tasks, key=lambda t: (PRIORITY_ORDER[t["priority"]], t["added"]))

    if 1 <= num <= len(sorted_tasks):
        task = sorted_tasks[num - 1]
        task["done"] = True
        save_tasks(tasks)
        print(f"  ✔  \"{task['title']}\" marked as done!")
    else:
        print("  ⚠  Task number out of range.")


def delete_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("\n  Delete task # (0 to cancel): "))
    except ValueError:
        print("  ⚠  Please enter a number.")
        return

    if num == 0:
        return

    sorted_tasks = sorted(tasks, key=lambda t: (PRIORITY_ORDER[t["priority"]], t["added"]))

    if 1 <= num <= len(sorted_tasks):
        task = sorted_tasks[num - 1]
        tasks.remove(task)
        save_tasks(tasks)
        print(f"  🗑  \"{task['title']}\" deleted.")
    else:
        print("  ⚠  Task number out of range.")


def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    removed = before - len(tasks)
    save_tasks(tasks)
    print(f"  🧹  Removed {removed} completed task(s).")


# ── Menu ───────────────────────────────────────────────────────────────────

def print_menu():
    print("\n  What do you want to do?")
    print("  [1] View tasks")
    print("  [2] Add a task")
    print("  [3] Mark a task as done")
    print("  [4] Delete a task")
    print("  [5] Clear all completed tasks")
    print("  [q] Quit")


def main():
    tasks = load_tasks()
    print("\n  Welcome to your To-Do List! 🎉")

    while True:
        print_menu()
        choice = input("\n  > ").strip().lower()

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_completed(tasks)
        elif choice in ("q", "quit", "exit"):
            print("\n  Bye! Stay productive 👋\n")
            break
        else:
            print("  ⚠  Invalid choice — try 1-5 or q.")


if __name__ == "__main__":
    main()

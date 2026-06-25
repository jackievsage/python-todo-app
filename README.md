# ✅ To-Do List CLI

A beginner-friendly command-line to-do app written in Python.

## Features
- Add tasks with a title and priority (High / Medium / Low)
- Mark tasks as done (shown with strikethrough)
- Delete individual tasks
- Clear all completed tasks at once
- Tasks are **saved automatically** to `tasks.json` — they persist between sessions!
- Tasks are sorted by priority, then by when they were added

## How to run

```
python todo.py
```

No external libraries needed — uses only the Python standard library (`json`, `os`, `datetime`).

## Concepts practiced

| Concept | Where |
|---|---|
| Functions | Every action is its own `def` |
| Lists & dicts | Tasks are stored as a list of dictionaries |
| File I/O | `load_tasks()` and `save_tasks()` using `json` |
| Sorting | `sorted()` with a custom `key=` lambda |
| User input & loops | The main menu `while True` loop |
| String formatting | f-strings throughout |

# daily_reminder.py

# Step 1: Get input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Prepare base message using match-case
match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base = f"Note: '{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority"

# Step 3: Add time-sensitivity detail
if time_bound == "yes":
    message = base + " that requires immediate attention today!"


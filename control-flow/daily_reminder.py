# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print("\nReminder:")
# Process the task based on priority and time sensitivity
try:
    match priority.lower():
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    # Modify reminder based on time-bound status using if statement
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Print the customized reminder
    print(f"Reminder: {reminder}")

except NameError:
    # Fallback for Python versions that do not support match statement
    if priority.lower() == 'high':
        reminder = f"'{task}' is a high priority task"
    elif priority.lower() == 'medium':
        reminder = f"'{task}' is a medium priority task"
    elif priority.lower() == 'low':
        reminder = f"'{task}' is a low priority task"
    else:
        reminder = f"'{task}' has an unknown priority"

    # Modify reminder based on time-bound status using if statement
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Print the customized reminder
    print(f"Reminder: {reminder}")

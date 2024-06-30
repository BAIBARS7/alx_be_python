# Prompting for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

# Processing the task based on priority and time sensitivity
try:
    match priority.lower():
        case 'high':
            reminder = f"High priority task: '{task}'"
        case 'medium':
            reminder = f"Medium priority task: '{task}'"
        case 'low':
            reminder = f"Low priority task: '{task}'"
        case _:
            reminder = f"Task with unknown priority: '{task}'"

    # Modifying reminder based on time-bound status using if statement
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Printing the customized reminder
    print(reminder)

except NameError:
    # Fallback for Python versions that do not support match statement
    if priority.lower() == 'high':
        reminder = f"High priority task: '{task}'"
    elif priority.lower() == 'medium':
        reminder = f"Medium priority task: '{task}'"
    elif priority.lower() == 'low':
        reminder = f"Low priority task: '{task}'"
    else:
        reminder = f"Task with unknown priority: '{task}'"

    # Modifying reminder based on time-bound status using if statement
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Printing the customized reminder
    print(reminder)

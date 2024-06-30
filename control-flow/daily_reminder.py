# Prompting for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Processing the task based on priority and time sensitivity using match case
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

    # Modifying reminder based on time-bound status
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Printing the customized reminder
    print(reminder)

except SyntaxError:
# Fallback for Python versions that do not support match statement
    if priority.lower() == 'high':
        reminder = f"High priority task: '{task}'"
    elif priority.lower() == 'medium':
        reminder = f"Medium priority task: '{task}'"
    elif priority.lower() == 'low':
        reminder = f"Low priority task: '{task}'"
    else:
        reminder = f"Task with unknown priority: '{task}'"

    # Modifying reminder based on time-bound status
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    # Printing the customized reminder
    print(reminder)

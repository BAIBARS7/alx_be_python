# Prompting for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Processing the task based on priority and time sensitivity
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

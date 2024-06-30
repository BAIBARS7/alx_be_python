# Prompting for task details
task = input("Enter task description: ")
priority = input("Enter task priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Processing the task based on priority and time sensitivity
if priority == 'high':
    reminder = f"High priority task: '{task}'"
elif priority == 'medium':
    reminder = f"Medium priority task: '{task}'"
elif priority == 'low':
    reminder = f"Low priority task: '{task}'"
else:
    reminder = f"Task with unknown priority: '{task}'"

# Modifying reminder based on time-bound status
if time_bound.lower() == 'yes':
    reminder += " that requires immediate attention today!"

# Printing the customized reminder
print(reminder)

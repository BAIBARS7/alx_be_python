def main():
  # Prompt for task and priority
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ").lower()
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Reminder message based on priority
  reminder = f"'{task}' is a {priority} priority task. "
  match priority:
    case "high":
      reminder += "Don't forget to complete it!"
    case "medium":
      reminder += "Consider completing it when you have a chance."
    case "low":
      reminder += "Consider completing it when you have free time."

  # Add urgency message for time-bound tasks
  if time_bound == "yes":
    reminder += " It requires immediate attention today!"

  # Print the reminder
  print(reminder)

if __name__ == "__main__":
  main()

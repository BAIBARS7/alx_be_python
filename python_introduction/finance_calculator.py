# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: $"))

# Ask for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: $"))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate projected annual savings after one year with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Output results
print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings after one year with 5% interest: ${projected_savings:.2f}")

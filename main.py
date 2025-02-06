
# This program will calculate expenses and expendetures



# Ask for monthly allowance and expenses in different categories
income = float(input("What is your monthly income? $"))
food = float(input("What is your monthly food spending? $"))
clothes = float(input("What is your monthly clothing spending? $"))
entertainment = float(input("What is your monthly entertainment spending? $"))


# Calculate total expenses and remaining balance
expenses = income + food + clothes + entertainment
balance = income - expenses


# Display results
print(f"Your income is: ${income:.2f}")
print(f"Your expenses total: ${expenses:.2f}")
print(f"Remaining is : ${balance:.2f}")


# Conditional message based on balance (depending on whether you overspent or underspent or spent just the right amount, write a specific message - try to be kind!)
print("Savings Goal Calculator")

goal = float(input("Enter your savings goal: $"))
current = float(input("How much have you saved already? $"))
monthly = float(input("How much will you save each month? $"))

if goal <= 0 or current < 0 or monthly <= 0:
    print("Please enter valid amounts.")
elif current >= goal:
    print("You already reached your savings goal!")
else:
    months = 0
    while current < goal:
        current += monthly
        months += 1

    print(f"It will take {months} month(s) to reach your goal.")
    print(f"Your savings will be ${current:.2f}.")

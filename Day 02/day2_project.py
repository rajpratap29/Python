# Bill Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give? 10, 15 or any number: "))
people = int(input("How many people to split the bill?: "))

final_bill = round((bill + ((bill / 100) * tip)) / people, 2)
print(f"Each person should pay: ${final_bill}")
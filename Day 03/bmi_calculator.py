height = float(input("Enter your height in meters e.g: 1.70: "))
weight = float(input("Enter your weight in kilograms e.g: 60:  "))

bmi = weight / (height ** 2) 

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are overweight.")
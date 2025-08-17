print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print(f"Ticket price will be ${bill}")
    elif age >= 12 and age < 18:
        bill = 7
        print(f"Ticket price will be ${bill}")
    else:
        bill = 5
        print(f"Ticket price will be ${bill}")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        print(f"Final ticket price will be ${bill + 3}")
else:
    print("Sorry, you have to grow taller before you can ride!")
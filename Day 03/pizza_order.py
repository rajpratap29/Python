print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_mid_large = 3
cheese = 1
bill = 0
if size == "S":
    bill = bill + small_pizza
elif size == "M":
    bill = bill + medium_pizza
else:
    bill = bill + large_pizza

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + pepperoni_small
    else:
        bill = bill + pepperoni_mid_large
        
if extra_cheese == "Y":
        bill = bill + cheese


print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: {bill}")
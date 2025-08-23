import math

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

input_height = int(input("Enter height of wall: "))
input_width = int(input("Enter width of wall: "))
# One can of paint can cover 5 square meter wall
coverage = 5 
paint_calc(height = input_height, width = input_width, cover=coverage)
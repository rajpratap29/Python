year = int(input("Enter a Year: "))
if year % 400 == 0:
    print(f"Year {year} is Leap Year.")
elif year % 100 == 0:
    print(f"Year {year} is not Leap Year.")
elif year % 4 == 0:
    print(f"Year {year} is Leap Year.")
else:
    print(f"Year {year} is not Leap Year.")
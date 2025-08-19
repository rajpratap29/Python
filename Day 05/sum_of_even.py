target = int(input("Enter a number till where you want sum of even: "))

sum = 0
for n in range(0, target + 1):
    if n % 2 == 0:
        sum += n
print(f"The sum of even is: {sum}")
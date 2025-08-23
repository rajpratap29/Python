def prime_check(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"The {number} is a prime number.")
    else:
        print(f"The {number} is not a prime number.")


n = int(input("Enter a number to check if it is prime or not: "))
prime_check(number = n)
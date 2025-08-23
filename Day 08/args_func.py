def sum(a, b):
    return a + b

print(sum(1,2))

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Raj")

# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Raj", "Saharanpur")
greet_with(location="Delhi", name="Raj")
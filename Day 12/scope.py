enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # Cannot access outside the function because it is inside the function scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy) # Will work here because it is inside the function

# print(new_enemy) # Will not work because it is outside the function
# In python block scope only exist for functions

# How to modify global scope

enemy = "Skeleton"
def increase_enemy():
    global enemy # This line refers to global scope enemy variable
    enemy = "Zombie"
    print(f"Enemy inside function: {enemy}")

increase_enemy()
print(f"Enemy outside function: {enemy}")


PI = 3.14259
URL = "https://www.google.com"
LINKEDIN = "https://www.linkedin.com/in/rajpratap29/"

# Uppercase means do not modify the variable
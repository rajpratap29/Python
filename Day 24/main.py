with open("Day 24/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("Day 24/my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

with open("Day 24/new_file.txt", mode="w") as file:
    file.write("New text.")
    
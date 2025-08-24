def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    # The above line is docstring it is a documentation of function
    if f_name == "" or l_name == "":
        return "You did'nt provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
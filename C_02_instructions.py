# functions go here
def yes_no(question):
    """checks if user response to question yes / no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(question).lower()

        if response in ['y', 'yes']:
            return "yes"

        elif response in ['n', 'no']:
            return "no"

        else:
            print("Please choose yes or no.")
            continue


def instructions():
    """Prints instructions."""

    print('''***** Instructions *****
    
Roll the dice and try to win
    ''')


# Main routine


want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()


print("we done")

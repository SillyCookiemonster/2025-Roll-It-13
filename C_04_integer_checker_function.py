# functions
def int_check(question):
    error = "Please enter and integer more than or equal to 13."

    try:
        response = int(input("What is the game goal? "))

        if response < 13:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# Main code
while True:
    game_goal = int_check("What is the game goal? ")
    print(game_goal)

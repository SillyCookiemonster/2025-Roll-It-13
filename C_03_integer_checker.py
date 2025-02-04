error = "Please enter and integer more than or equal to 13."

while True:
    try:
        game_goal = int(input("What is the game goal? "))

        if game_goal < 13:
            print(error)
        else:
            print(f"Game goal: {game_goal}")

    except ValueError:
        print(error)

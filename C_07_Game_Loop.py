# At the start of the game the player and computers score are both zero
user_points = 0
comp_points = 0

# Get game goal
game_goal = int(input("What is the ame goal? "))

# Play multiple round until the winner has been found
while user_points < 13 and comp_points < 13:
    # Start of round loop
    # For testing purposes, ask what the points for the user / computer were
    user_score = int(input("What is the score of the user? "))
    comp_score = int(input("What is the score of the computer? "))

    # Outside rounds loop - Update score with round points, only add points to the score of the winner
    if user_score > comp_score:
        user_points += user_score
    else:
        comp_points += comp_score

    # show overall scores (add this to the rounds loop)
    print("Round Points:")
    print(f"User: {user_score} | Computer: {comp_score}")
    print("Total Points:")
    print(f"User: {user_points} | Computer: {comp_points}")

# end of entire game, output final results
print("End of game")
print("Total Points:")
print(f"User: {user_points} | Computer: {comp_points}")
if user_points > comp_points:
    print("The user won!")
else:
    print("The comp won")

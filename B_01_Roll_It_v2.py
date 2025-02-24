import random


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


def int_check(question):
    """Checks if the integer is more than or equal to 13"""
    error = "Please enter and integer more than or equal to 13."

    while True:

        try:
            response = int(input(question))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


def statement_generator(statement, decoration):
    """Add decorations to the start and end of headings"""
    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


# Main code

# At the start of the game the player and computers score are both zero
user_points = 0
comp_points = 0

rounds_played = 0
user_score = 0
comp_score = 0

# Initialize list to hold game history
game_history = []

statement_generator("Welcome to the Roll It 13 Game", "🍀")

# Asks the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()
print()
# Get game goal
game_goal = int_check("What is the game goal? ")

while user_score < game_goal and comp_score < game_goal:
    # Play multiple round until the winner has been found

    rounds_played += 1
    # Start of round loop
    statement_generator(f"Round {rounds_played}", "🎲")
    # Roll the dice for the user and note if they got double
    initial_user = initial_points("User")
    initial_comp = initial_points("Computer")

    # retrieve user points
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points!")

    # assume user goes first
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer!\n")

    # if the points are equal then the user starts
    elif user_points == comp_points:
        print("The initial points were the same, so the user starts!")

    # if the computer has fewer points, then switch computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have a winner
    while player_1_points < 13 and player_2_points < 13:
        input("Press <enter> to continue this round. ")
        print()

        # first person rolls and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} and has {player_1_points} points.")

        #     if the first players score is over 13, end the loop
        if player_1_points >= 13:
            print(f"{player_1_points} has won the game!")
            break

        # second person rolls and score is updated
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: rolled a {player_2_roll} and has {player_2_points} points.")

        # if the second players score is over 13, end the loop
        if player_2_points >= 13:
            break

        print(f"{first}: {player_1_points} | {second}: {player_2_points}.")

    # end of round

    # associate the user and computer points if the computer went first
    if first == "Computer":
        comp_points = player_1_points
        user_points = player_2_points
    else:
        comp_points = player_2_points
        user_points = player_1_points

    # work out who won...
    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s scores have been reset to zero."

    # double user points if available
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2
        user_score += user_points
    elif winner == "user":
        user_score += user_points
    else:
        comp_score += comp_points

    # Outside rounds loop - Update score with round points, only add points to the score of the winner
    # if user_points > comp_points:
    #     user_points += user_points
    # else:
    #     comp_points += comp_points

    # add round to history
    game_results = (f"Round {rounds_played}: User points {user_points} | "
                   f"Computer Points {comp_points}, {winner} wins ({user_points}|{comp_points})")
    game_history.append(game_results)

    # show overall scores (add this to the rounds loop)
    game_score = f"User: {user_score} | Computer: {comp_score}"
    statement_generator("Game Update", "*")
    print(game_score)
    # player_1_points, player_2_points = 0, 0
    # break


# end of entire game, output final results
statement_generator("Game over", "🏁")

if user_points > comp_points:
    statement_generator("The user won!", "👍")
else:
    statement_generator("The computer won", "🤖")

statement_generator("game History", "📃")

for item in game_history:
    print(item)


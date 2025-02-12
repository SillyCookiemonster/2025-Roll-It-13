import random


# functions

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

# Roll the dice for the user and note if they got double
initial_user = initial_points("user")
initial_comp = initial_points("comp")

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

# if user has less points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer!\n")

# if the points are equal then the user starts
if user_points == comp_points:
    print("The initial points were the same, so the user starts!")

# if the computer has fewer points, then switch computer to 'player 1'
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

# loop until we have a winner
while player_1_points < 13 and player_2_points < 13:
    input("\nPress <enter> to continue this round. ")
    print()

    # first person rolls and score is updated
    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll

    print(f"{first}: rolled a {player_1_roll} and has {player_1_points} points.")

    #     if the first players score is over 13, end the loop
    if player_1_points >= 13:
        break

    # second person rolls and score is updated
    player_2_roll = random.randint(1, 6)
    player_2_points += player_2_roll

    print(f"{second}: rolled a {player_2_roll} and has {player_2_points} points.")

    # if the second players score is over 13, end the loop
    if player_2_points >= 13:
        break

    print(f"{first}: {player_1_points}  |   {second}: {player_2_points}.")

# end of round

# associate the user and computer points if the computer went first
if first == "Computer":
    player_1_points, player_2_points = player_2_points, player_1_points

# work out who won...
if player_1_points > player_2_points:
    winner = "user"
else:
    winner = "computer"

round_feedback = f"The {winner} won."

# double user points if available
if winner == "user" and double_user == "yes":
    player_1_points = player_1_points * 2

# output results
statement_generator("Round Results", "=")
print(f"User points: {player_1_points} | Computer points: {player_2_points}")
print(round_feedback)
print()

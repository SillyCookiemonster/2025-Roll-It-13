# Initialize list to hold game history
game_history = []

# get data (for testing purposes)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break
    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input("Who won? ")
    user_score = int(input("User score: "))
    comp_score = int(input("Computer score: "))

    game_results = (f"Round {rounds_played}: User points {user_points} | "
                   f"Computer Points {comp_points}, {winner} wins ({user_points}|{comp_points})")
    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)

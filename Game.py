import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Entner the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2-4")
    else:
        print("Invalid input")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) <= max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("your total score is: ", players_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn Done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("your score is: ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is: ", players_scores[player_idx])

max_score = max(players_scores)
winner_idx = players_scores.index(max_score)
print("The winner is ", winner_idx + 1, "and your total score is: ", max_score)

game_summary = []
guess_stats = []

rounds_lost = 0

rounds_played = 5
guesses_allowed = 3

for item in range(0,5):
    num_guesses = input("choose num guesses: ")
    if num_guesses > guesses_allowed:
        outcome = "Oh No!"
    else:
        outcome = "success"

    outcome = "Round {}: Guesses: {} | Result: {}".format(item, num_guesses, outcome)

    # outcome for game history
    game_summary.append(outcome)

    # list to work out best, worst and average number of guesses
    guess_stats.append(num_guesses)

rounds_won = rounds_played - rounds_lost

# **** Calculate Game Stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


print()
print("***** Game History ******")
for game in game_summary:
    print(game)

print()

# work out best (lowest number of guesses), worst and average

# displays game stats with % values to the nearest whole number
print("***** Game Statistics *****")
print("Best: ")
print("Worst: ")
print("Average: ")
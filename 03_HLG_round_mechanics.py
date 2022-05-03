# Function used to check input is valid


# Check for an integer more than 0
def num_check(question):
    while True:
        response = input(question)

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0 "
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here....

rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many rounds? <enter> for infinite mode")

end_game = "no"
while end_game == "no":
    # Start of game play loop

    rounds_played +=1

    # Rounds Heading
    print()
    if rounds == "":
            heading = "Continuous Mode:"
            "Round {}".format(rounds_played)

    else:
            heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)
    guess = input("Guess")  # replace with call to number checking function
    
    # end game if exit code is typed
    if guess == "xxx":
        break
    elif rounds_played == rounds:
        break

    # rest of loop / game
    print("You guess {}".format(guess))

    # end game if required

print("Thank you for playing")


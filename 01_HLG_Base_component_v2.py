# Function used to check input is valid


# Check for an integer more than 0
def num_check(question):
    while True:
        response = input(question).lower()

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0 "

        if response == "" or response =="xxx":
            return response

        else:
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

if rounds == "":
    mode = "infinite"
    # set rounds to a number!!
    rounds = 10
else:
    mode = "regular"

end_game = "no"
while end_game == "no":
    # Start of game play loop

    if end_game == "yes":
        break

    # ends game if number of requested rounds has been played
    rounds_played +=1
    
    if rounds_played == rounds + 1:
        break

    # Rounds start here

    secret = 7  # replace with secret number in due course

    # Rounds Heading
    print()


    if mode == "infinite":
            heading = "Continuous Mode:"
            "Round {}".format(rounds_played)
            rounds += 1

    else:
            heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)


    guess = ""
    # guessing for the round goes here
    while guess != secret:
    #  Guessing starts here...

        guess = num_check("Guess")  # replace with call to number checking function
        
        # end game if exit code is typed
        if guess == "xxx":
            end_game = "yes"
            break
            
        # elif rounds_played == rounds:
        #     end_game = "yes"
        #     break

        # check user guess


        # rest of loop / game
        print("You guessed: {}".format(guess))

    # end game if required

print("Thank you for playing")


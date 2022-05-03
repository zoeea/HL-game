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
import random
import math

def check_rounds():
    while True:

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n "

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # if response is too low, go bak to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue
        
        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()

def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

# outputs instructions, returns ""
def instructions():
    print(""" 
        *** Instructions ****
        *****To begin with the computer will ask you to choose a number of rounds OR press <enter> for enfinite mode****
        *****Next you will guess a number , once selecting what numbers you will be guessing between(high and low number)***
        *****If your number is too high the computer will tell you to go lower , and visa versa, until you guess the correct number****
          """)

    return ""

# ******* MAIN ROUTINE STARTS HERE  ***********

# intialise game parameters etc
rounds_played = 0



# welcome user
print("**** Welcome to the great higher or lower Game *****")
print()

# ask user if they need instructions...
played_before = choice_checker("Have you played the game before? ", ["yes", "no"], "Please enter yes or no")

if played_before == "no":
    instructions()

# get game parameters (loc, high)
rounds = 3      # replace with question asking how many rounds (etc)

# ask for low / high number

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


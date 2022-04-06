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
    print(""" *** Instructions ****

    
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



# ***** Main Routine ******

# Ask user for # of rounds..
print()
rounds = intcheck("How many rounds <enter> for infintite: ", 1, exit_code = "")

if rounds == "":
    print("you chose infinite mode")
else:
    print("you asked for {} rounds".format(rounds))

# checks that response is an integer    
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = intcheck("High Number: ", low_num)
print("You chose a high number of ", high_num)

# works out max guesses based on user selected range
range = high_num - low_num + 1
max_raw = math.log2(range)  #finds maximum # of guesses using
max_upped = math.ceil(max_raw)  #rounds up ( ceil -> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

print()


end_game = "no"
while end_game == "no":
# Start of game play loop
# ask user if they want to play infinite mode or how many rounds
    rounds_played +=1

    # Rounds Heading
    print()
    if rounds == "":
            heading = "Continuous Mode:"
            "Round {}".format(rounds_played)

    else:
            heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)

    secret = random.randint(low_num, high_num)
    print("spoiler alert: ", secret)
    print()
    
    guess = ""
    while guess != secret:
        guess = int(input("Guess: "))  # replace with number checker in due course

        # end game if exit code is typed
        if guess == "xxx":
            break
        elif rounds_played == rounds:
            break

        if guess < secret:
            print("guess higher")
        elif guess > secret:
            print("guess lower")
        else:
            print("You have guessed the correct number! ")
            break


    



    # rest of loop / game
    print("You guess {}".format(guess))

    


    # ask user if they would like to pick the numbers to guess between


    # end game if required

print("Thank you for playing")

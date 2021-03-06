import math
import random

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
                                                    *** Instructions ***

    **To begin with the computer will ask you to choose a number of rounds OR press <enter> for infinite mode**
    **Next you will guess a number , once selecting what numbers you will be guessing between(high and low number)**
    **If your number is too high the computer will tell you to go lower , and visa versa, until you guess the correct number**
     
      """)

    return ""

# Main routine goes here....


# intialise game parameters etc
rounds_played = 0

all_game_guesses = []



# welcome user
print()
print("**** Welcome to the great higher or lower Game *****")
print()

# ask user if they need instructions...
played_before = choice_checker("Have you played the game before? ", ["yes", "no"], "Please enter yes or no")
print()

if played_before == "no":
    instructions()

# ask for low / high number
# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many rounds? <enter> for infinite mode")

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

    numbers_guessed = []

    secret = random.randint(low_num, high_num)

    # Rounds Heading
    print()


    if mode == "infinite":
            heading = "Continuous Mode:"
            "Round {}".format(rounds_played)
            rounds += 1

    else:
            heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)

    # works out max guesses based on user selected range
    range = high_num - low_num + 1
    max_raw = math.log2(range)  #finds maximum # of guesses using
    max_upped = math.ceil(max_raw)  #rounds up ( ceil -> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    guess = ""
    while guess != secret and len(numbers_guessed) < max_guesses:
        guess = intcheck("Guess: ", low_num, high_num, "xxx")  # replace with number checker in due course


        # end game if exit code is typed
        if guess == "xxx":
            end_game = "yes"
            break
        
        else:
            numbers_guessed.append(guess)

        if guess < secret:
            print("guess higher")
        elif guess > secret:
            print("guess lower")
        else:
            print("You have guessed the correct number! ")
            break

    all_game_guesses.append(len(numbers_guessed))


print("all guesses", all_game_guesses)

#finding smallest number
s_num = min(all_game_guesses)
s_num_max = max(all_game_guesses)
average = sum(all_game_guesses) / len(all_game_guesses)

print ("The smallest number of gueeses in any given round was: ", s_num)
print ("The largest number of gueeses in any given round was: ", s_num_max)
print ("Average number of guesses per round: {}".format(average))

print("Thank you for playing !!")


#Hl componenet 1 - Get (and check) user input

# To Do 
# Check a lowest is an interger (any interger)
# Check that highest is more than lowest (lower bound only)
# check that rounds is more than 1(upper bound only)
# Check that guess is between lowest and highest (lower and upper bound)



# Number checking function goes here 
def int_check(question, low=None, high=None):

# main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1 )
rounds = int_check("rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)


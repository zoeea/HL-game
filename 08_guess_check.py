secret = 7

guess = ""
while guess != secret:
    guess = int(input("Guess: "))  # replace with number checker in due course

    if guess < secret:
        print("guess higher")
    elif guess > secret:
        print("guess lower")
    else:
        print("You have guessed the correct number! ")
        break

print("we are done")

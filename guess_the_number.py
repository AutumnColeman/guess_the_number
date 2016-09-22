import random
secret_number = random.randint(1, 10)
tries = 5
play_again = "y"

while play_again != "n":
    guess = int(raw_input("I am thinking of a number between 1 and 10. What's the number? "))
    while (guess != secret_number) and tries > 1:
        if guess > secret_number:
            tries = tries - 1
            print ("%d is too high.") % guess

        elif guess < secret_number and tries > 1:
            tries = tries - 1
            print ("%d is too low") % guess

        print ("You have %d guesses left") % tries
        guess = int(raw_input("What's the number? "))

    if guess != secret_number:
                print "You ran out of guesses!"

    else:
            print "Yes! You win!"

    play_again = (raw_input("Do you want to play again (Y or N)? ")).lower()

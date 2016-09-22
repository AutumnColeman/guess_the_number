print "I am thinking of a number between 1 and 10."
secret_number = 5
guess = int(raw_input("What's the number? "))

while (guess != 5):
    if guess > 5:
        print ("%d is too high.") % guess
        guess = int(raw_input("What's the number? "))

    elif guess < 5:
        print ("%d is too low") % guess
        guess = int(raw_input("What's the number? "))

else:
    print "Yes! You win!"

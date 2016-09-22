import random
secret_number = random.randint(1, 10)
guess = int(raw_input("I am thinking of a number between 1 and 10. What's the number? "))

while (guess != secret_number):
    if guess > secret_number:
        print ("%d is too high.") % guess
        guess = int(raw_input("What's the number? "))

    elif guess < secret_number:
        print ("%d is too low") % guess
        guess = int(raw_input("What's the number? "))

else:
    print "Yes! You win!"

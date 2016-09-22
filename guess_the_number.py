print "I am thinking of a number between 1 and 10."
secret_number = 5
guess = int(raw_input("What's the number? "))

while (guess != 5):
    print "Nope, try again."
    guess = int(raw_input("What's the number? "))

else:
    print "Yes! You win!"

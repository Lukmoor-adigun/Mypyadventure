import random
print('I am thinking of a number between 1 and 20, Take a guess.\nYou have 6 tries')
secret_number = random.randint(1,20)

#ask the user to guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
# letting the program provide random guesses.
    guess = random.randint(1,20)
    print(guess)

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break
if guess == secret_number and guessTaken < 2:
    print('You got the answer in ' + str(guessTaken) + ' guess')
elif guess == secret_number:
    print('You got the answer in ' + str(guessTaken) + ' guesses')
else:
    print('The number i was thinking of is ' + str(secret_number))
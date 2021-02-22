import random

print("Hi what is your name?")
name = input()

print(f"welcome {name}, i am thinking of number between 1 and 20")
secretNumber = random.randint(1, 20)

for guessnumber in range(1, 6):
    guess = int(input("Enter Number: "))

    if guess > secretNumber:
        print('Number is too high')
    elif guess < secretNumber:
        print('Number is too low')
    else:
        # this condition for correct guess
        break

if guess == secretNumber:
    print(f"your guess is correct in {guessnumber} times")
else:
    print(f"Nope Number is {secretNumber}")

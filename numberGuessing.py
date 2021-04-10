import random

number = random.randint(0, 100)
tries = 0

u_name = input("Please, enter your name: ")
u_name.strip()

print(f"Hello! Welcome {u_name}")
print(f"Would you like to play game with me {u_name}?")
print("1) Yes")
print("2) No")

option = input("Select your option: ")
option = int(option)

if option == 1:
    print("I\'am thinking a number between 0-100")
    print("You have to guess the number in five tries")

    guess = input("Guess a number: ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("Guess lower dude...")
    if guess < number:
        print("Guess higher my friend...")

    while guess != number and tries < 5:
        guess = input("Try again fella: ")
        guess = int(guess)
        tries += 1

        if guess > number:
            print("Guess lower dude...")
        if guess < number:
            print("Guess higher my friend...")

    if guess == number:
        print(f"YOU WON!!! Number of tries: {tries}")

    else:
        print("You lost idiot hahahahaha")
        print(number)

elif option == 2:
    print("Thank you :)")

else:
    print("Invalid Option!")

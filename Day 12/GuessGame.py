import random

number = random.randint(1,100)
success = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard': \n")
if dif == "easy" or dif == "Easy":
    lives = 10
elif dif == "hard" or dif == "Hard":
    lives = 5

for i in range(0,lives):
    guess = int(input("Make a guess: \n"))
    if guess == number:
        print(f"You Guessed it ! The number was {number} !")
        success = True
        break
    elif guess > number and (guess - number) < 5:
        print("Slightly high, go a little bit lower.")
    elif guess < number and (number - guess) < 5:
        print("Slightly low, go a little bit higher.")
    elif guess > number and (guess - number) > 5 and (guess - number) < 15:
        print("High, go lower.")
    elif guess < number and (number - guess) > 5 and (number - guess) < 15:
        print("Low, go higher")
    elif guess > number:
        print("Too High, go down.")
    elif guess < number:
        print("Too Low, go up.")
    else:
        print("what the hell.")

if success != True: 
    print("Game Over")
    print(f"The number was {number}")
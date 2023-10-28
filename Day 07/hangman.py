import random
player_lives = 5
words = ["appearance","park","scenery","landslideinator"]

word = words[random.randint(0,3)]

display = []

for i in range(len(word)):
    display.append("_")

choice = input("Hi there ! Would you like to play Hangman ?: \n")
    
if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
    print(f"The word you have to guess is a {len(word)} letter word: \n")

    while player_lives > 0:
        if "_" not in display:
            print("Congrats you won !")
            break
        print(display)
        guess = input("Enter your guess: \n")
        
        for i in range(len(word)):
            
            if guess == word[i]:
                print(word[i])
                display[i] = word[i]
                
        if guess not in word:
            print("Sorry, not in the word. Guess again.")
            player_lives -= 1
            print(f"You have {player_lives} remaining.")
    if player_lives == 0:
        print("Sorry, no more lives. You lost.")
else:
    print("Alright, bye.")
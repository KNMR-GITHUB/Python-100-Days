print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

cross_road = input("You're at a cross road. Where do you want to go? \nType: 'left' or 'right'\n")

if cross_road == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. \nType: 'wait' to wait for a boat or 'swim' to swim across.\n")

    if lake == "wait":
        door = input("You reached the island. And entered the mansion. There are 3 doors. A red, blue and green door. Which door should you go in ?\nType: 'red' for red door,'blue' for blue door or 'green' for green door\n")
        if door == 'green':
            print("You won. Bye.")
        elif door == "blue":
            print("You won. Maybe, I don't know. Bye")
        elif door == 'red':
            print("You lost. Sad.")
        else:
            print("U is LoSe, SEd lYFe.")
    elif lake == "swim":
        print("You swam to the island. You reached the island, but you see a sign that says 'Nuclear Waste', you die of radiation.\n----Game Over---- ")
    else:
        print("The ghost of 'there is a third option', caught you. And you died.\n----Game Over----")
elif cross_road == "right":
    print("A truck hit you. You ded. \n----Game Over----")     
else:
    print("You got yourself caught in a tax fraud. You are in jail.\n----Game Over----")
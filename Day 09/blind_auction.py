import os
print("Welcome to the secret auction program.")
bidders = "boi"
bList = []
i = 0
max = 0
while bidders != "n":
    name = input("What is your name?: \n")
    bid = int(input("What's your bid?: \n"))
    bList.append({"name": name, "bid": bid})
    i+= 1
    
    bidders = input("Are there any more bidders?: (y/n)")
    if bidders == 'y':
        os.system("cls")

for k in range(0,len(bList)):
    if bList[k]["bid"] > max:
        max = bList[k]["bid"]
        winner = bList[k]["name"]

print(f"The winner is {winner} with a bid of ${max}.")
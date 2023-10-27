import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
pCards = []
dCards = []
score = [0,0]
def dealCards():
    x = random.randint(0,12)
    return cards[x]

def showCards(pCards,dCards):
    print(f"Player Cards: [{pCards}]")
    print(f"Player score: {score[0]}")
    print(f"Dealer Cards: [{dCards[0],'X'}]")

def showCard(pCards,dCards):
    print(f"Player Cards: [{pCards}]")
    print(f"Player score: {score[0]}")
    print(f"Dealer Cards: [{dCards}]")
    print(f"Dealer Cards: [{score[1]}]")


def scores(pCards,dCards):
    score[0] = (sum(pCards))
    score[1] = (sum(dCards))


Play_No_Play = input("Would you like to play a game of Black Jack ? \n 1)'yes' 2)'no'\n")
if Play_No_Play == 'y' or Play_No_Play == 'Y' or Play_No_Play == 'yes' or Play_No_Play == 'Yes' or Play_No_Play == 'YES':
    pCards.append(dealCards())
    dCards.append(dealCards())

    scores(pCards,dCards)

    showCards(pCards,dCards)

    while score[0] < 21:
        pChoice = input("Would you like to : \n 1) 'Deal' or 2) 'Hold'\n")

        if pChoice == 'Deal' or pChoice == 'deal' or pChoice == 'DEAl' or pChoice == '1':
            pCards.append(dealCards())
            if len(dCards) == 1:
                dCards.append(dealCards())

            scores(pCards,dCards)
            showCards(pCards,dCards)

            if score[0] == 21:
                showCard(pCards,dCards)
                print("P wins")
                break
            elif score[1] == 21:
                showCard(pCards,dCards)
                print("d wins")

            elif score[0] > 21:
                # do something
                for i in range(0,len(pCards)):
                    if pCards[i] == 11:
                        pCards[i] = 1

                scores(pCards,dCards)

                if score[0] > 21:
                    showCard(pCards,dCards)
                    print("d wins")

                else:
                    continue
            else:
                continue
        elif pChoice == 'Hold' or pChoice == 'hold' or pChoice == 'HOLD' or pChoice == '2':
            
            if score[1] > score[0]:
                showCard(pCards,dCards)
                print("d wins")
            else:
                if score[0] > score[1] and score[1] > 17:
                    showCard(pCards,dCards)
                    print("p wins")
                else:
                    while score[1] < 17:
                        dCards.append(dealCards())
                        scores(pCards,dCards)

                        if score[1] > 21:
                            showCard(pCards,dCards)
                            print("p wins")
                            break

                        elif score[1] > score[0]:
                            showCard(pCards,dCards)
                            print("d wins")
                            break
                        elif score[1] < score[0] and score[1] > 17:
                            showCard(pCards,dCards)
                            print("p wins")
                            break
                        else:
                            continue
            break

else:
     print("Alright then, bye.")
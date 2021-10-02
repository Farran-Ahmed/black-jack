import random
playerIn = True
dealerIn = True
#black jack

#deck of cards/ player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A',]
playerhand = []
dealerhand = []
#deal the cards
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
#caculate  the total of each hand
def total(turn):
    total = 0 
    face ='J', 'K', 'Q'
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11 
    return total
            
#check for winner
def revealdealerhand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]

#game loop
for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)
while  playerIn or dealerIn:
    print("Dealer had {revealDealerHand()} and X")
    print(f"You have {playerhand} for a total of {total(playerhand)}")
    if playerIn:
        stayOrhit = input ("1: Stay\n2: Hit\n")
    if total(dealerhand) > 16:
        dealerIn = False
    else:
        dealcard(dealerhand)
    if stayOrhit == '1':
        playerIn = False 
    else:
        dealcard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerhand) >= 21:
        break


if total(playerhand) == 21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Black-jack you win")
elif total(dealerhand) ==21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Black-jack Dealer wins") 
elif total(playerhand) > 21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You Bust! Dealer wins!")
elif total(dealerhand) > 21:
    (f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer busts! You win")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    (f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("dealer wins!")
elif 21 - total(dealerhand) > 21 -total(playerhand):
    (f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You Win")






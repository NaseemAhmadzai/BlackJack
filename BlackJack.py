# BlackJack

from random import randint
def makeDeck():
    '''
    This function genereates a deck of cards.
    params: nothing
    returns: a list of 52 tuples each representing a single card.
    '''
    #sets the card types and values
    cardValue = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suitValue = ['H','H','C','D']
    deck = []
    #This iterates all 52 cards into a deck
    for cValue in suitValue:
        for sValue in cardValue:
            deck.append(sValue + ' of ' + cValue)
    return deck



def cardValue(card):
    #only reading first slice to determine value of the card
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        #card[:1] example '2' out of the full '2 of H' string
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")


def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck,card):
    return deck.remove(card)


# I used /n in most places it just to print things in new line

play_Black_Jack = ''
while play_Black_Jack != 'EXIT':
    #deck creation, card creation, card removal from deck, values and totals
    new_deck = makeDeck()
    card1 = new_card(new_deck)
    remove_card(new_deck,card1)
    card2 = new_card(new_deck)
    remove_card(new_deck,card2)
    print ("\n\n\n\n" + card1 + " and " + card2) #doing this statement first allows for selection between 1 and 11
    valu1 = cardValue(card1)
    valu2 = cardValue(card2)
    total = valu1 + valu2
    print("with a total of " + str(total) )

    #dealer's hand
    dealer_card1 = new_card(new_deck)
    remove_card(new_deck,dealer_card1)
    dealer_card2 = new_card(new_deck)
    remove_card(new_deck,dealer_card2)
    dealer_value1 = cardValue(dealer_card1)
    dealer_value2 = cardValue(dealer_card1)
    dealer_total = dealer_value1 + dealer_value2
    print ("The dealer's first a " + dealer_card1)

    if total == 21:
        print("Blackjack!")
    else:
        while total < 21: #not win or loss yet
            answer = input("Would you like to hit or stand?\n> ")
            if answer.lower() == 'hit':
                #more card creation, removal, and value added to total
                more_card = new_card(new_deck)
                remove_card(new_deck,more_card)
                more_value = cardValue(more_card)
                total += int(more_value)
                print (more_card + " for a new total of " + str(total))
                if total > 21: #lose condition
                    print("You LOSE!")
                    play_Black_Jack = input("Would you like to continue? EXIT to leave\n")
                elif total == 21: #winning condition
                    print("You WIN BIG WIN WOO WOO")
                    play_Black_Jack = input("Would you like to continue? EXIT to leave\n")
                else:
                    continue
            elif answer.lower() == 'stand':
                print("The dealer nods and reveals his other card to be ")
                print("a " + dealer_card2 + " for a total of " + str(dealer_total))
                if dealer_total < 17:
                    print("The Dealer hits again.")
                    dealer_more = new_card(new_deck)
                    more_dealer_value = cardValue(dealer_more)
                    print("The card is a " + str(dealer_more))
                    dealer_total += int(more_dealer_value)
                    if dealer_total > 21 and total <=21:
                        print("Dealer Bust! You win!")
                    elif dealer_total < 21 and dealer_total > total:
                        print("Dealer has " + str(dealer_total) + " You lose!")
                    else:
                        continue
                elif dealer_total == total:
                    print("Equal Deals, no winner")
                elif dealer_total < total:
                    print("You win!")
                else:
                    print("You Lose!")
                play_Black_Jack = input("\nWould you like to continue? EXIT to leave\n")
                break
print("Thank you for Playing")

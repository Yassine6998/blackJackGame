# Import random module for the random numbers of black jack and time module and os module 
import random
import time
import os

# A variable for the numbers that can the dealer and the player choose from
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Define a function to clear the screen
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

# Make the blackjack ascii art in a variable
blackJackAsciiArt="""
_____                    _            ___             
|_   _|_      _____ _ __ | |_ _   _   / _ \ _ __   ___ 
  | | \ \ /\ / / _ \ '_ \| __| | | | | | | | '_ \ / _ \\
  | |  \ V  V /  __/ | | | |_| |_| | | |_| | | | |  __/
  |_|   \_/\_/ \___|_| |_|\__|\__, |  \___/|_| |_|\___|
                              |___/                    
"""

# A variable for the player cards and the dealer cards
playerCards=[]
dealerCards=[]

# Define a function to give distribute the cards in the beginning
def giveCards():
    # So we can edit the global variable
    global playerCards
    global dealerCards

    # Give the player and the dealer (computer) two random cards
    playerCards.extend(random.choices(cards, k=2)) # random.choices return a list
    dealerCards.extend(random.choices(cards, k=2))
 
# Define a function to check the Black Jack
def checkBlackJack(playerCards, dealerCards):
    # Check if the player got black jack and the dealer also 
    if sum(playerCards)==21 and sum(dealerCards)==21:
        print(f"You cards are {playerCards} with some {sum(playerCards)}")
        print(f"Computer's two cards are {dealerCards} with some {sum(dealerCards)}")
        print('Draw. Both got a Black Jack.')
        return 'stop'
    # Check if the player got a black jack 
    elif sum(playerCards)==21:
            print(f"You cards are {playerCards} with some {sum(playerCards)}")
            print(f"Computer's two cards are {dealerCards} with some {sum(dealerCards)}")
            print('Win. You got a Black Jack.')
            return 'stop'

# Define a function to manage the cards
def manageCards(playerCards, dealerCards): # High level function 

    # Show the cards
    print(f"Your cards are {playerCards} with sum {sum(playerCards)}")
    print(f"Computer's first card {dealerCards[0]}")
    
    # Check if your sum is not bigger than 21
    if sum(playerCards)<=21:
        if input('Get another card (y/n)? ').lower()=='y':
            # Add a random card to the player cards
            playerCards.append(random.choice(cards)) # 26
            # Check
            return manageCards(playerCards, dealerCards) # Low level function 

        else:
            # Give the dealer the right to play
                    while sum(dealerCards)<17:
                        dealerCards.append(random.choice(cards))

                    # Check if the dealer's sum bigger than 21
                    if sum(dealerCards)>21:
                        print(f"Your cards are {playerCards} with some {sum(playerCards)}")
                        print(f"Computer's two cards are {dealerCards} with some {sum(dealerCards)}")
                        print('Win. Dealer sum bigger than 21')
                        print('-------------\nThe game is over\n-------------')

                    else:
                        compareCards(playerCards, dealerCards)
                        print('-------------\nThe game is over\n-------------')
            
        
    else:
        # Check if he has an Ace
        if 11 in playerCards:
            # Replace it  by 1 and check 
            index=playerCards.index(11)
            playerCards[index]=1
            # Check again
            manageCards(playerCards, dealerCards)
        else:
            print('Lose. Your sum bigger than 21')
            return 'stop'
       
# Define a function to compare the cards
def compareCards(playerCards, dealerCards):
    if sum(playerCards)>sum(dealerCards):
        print(f"Your cards are {playerCards} with sum {sum(playerCards)}")
        print(f"Computer's cards {dealerCards} with sum {sum(dealerCards)}")
        print('Win. You sum bigger than dealer')
    elif sum(dealerCards)>sum(playerCards):
        print(f"Your cards are {playerCards} with sum {sum(playerCards)}")
        print(f"Computer's cards {dealerCards} with sum {sum(dealerCards)}")
        print('Lose. Dealer sum bigger than you')

    else:
        print(f"Your cards are {playerCards} with sum {sum(playerCards)}")
        print(f"Computer's first card {dealerCards} with sum {sum(dealerCards)}")
        print('Draw!')

# Define a function for the BlackJack game 
def game():


        # Check the user's choice to start any game
        gameChoice=input("""
Choose a game to start...
1. Froggy
2. Twenty One
3. Snake 
--------------\n                                 
""").lower()
        if gameChoice=='twenty one':

            # Clear the screen
            clearScreen()

            # Some time module tricks (Labor Illusion) and print the title and the ascii art
            print('Game starting...')

            time.sleep(2)

            print(blackJackAsciiArt)

            # Give a random cards to the player and the dealer
            giveCards()

            # Check what the black jack function returns after run it 
            if checkBlackJack(playerCards, dealerCards)=='stop':
                print('-------------\nThe game is over\n-------------')
            
            
            else:
                # Check what the manageCards function returns after run it
                if manageCards(playerCards, dealerCards)=='stop':
                    print('-------------\nThe game is over\n-------------')

        else:
            print('Sorry, now this game is unavailable!!!')
            print('Returning to the main....')
            time.sleep(2)
            game()

game()

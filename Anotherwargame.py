from random import shuffle
import time

class card:
    def __init__(self, suit, rank):
        self.suit = suit.lower()  #The order in which the cards are read
        self.rank = rank

    def isBlackOrRed(self):
        #Function to check if a card the black or red
        if self.suit == "hearts" or self.suit == "diamonds":
            return "red"
        else:
            return "black"

    def getDescription(self):
        #Returns a two item list
        return [self.rank, self.suit]

    def __repr__(self):
        #Explaining the cards
        rank = self.rank
        if rank == 1:
            rank = "ace"
        elif rank == 11:
            rank = "jack"
        elif rank == 12:
            rank = "queen"
        elif rank == 13:
            rank = "king"

        return "{} of {}".format(rank, self.suit)

class cardStack:
    #Class for both decks and hands
    def __init__(self, name=""):
        self.stack = []
        self.name = name

    def giveFullDeck(self):
        #A full stack of cards
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for suit in suits:
            for rank in range(1, 14):
                self.stack.append(card(suit, rank))

    def stackSize(self):
        #Return the length of the stack
        return len(self.stack)

    def shuffle(self, amount=1):
        # Shuffle the stack
        for i in range(0, amount):
            shuffle(self.stack)

    def deal(self, amount, stack, position=-1):
        # Dealing the card(s)
        for i in range(0, amount):
            dealt = self.stack[0:1]
            self.stack = self.stack[1:]
            for i in dealt:
                stack.stack.insert(position, i)

    def splitDeckIntoTwoStacks(self, stack1, stack2):
        # Split the deck into two
        while len(self.stack) > 0:
                self.deal(1, stack1)
                self.deal(1, stack2)

    def __str__(self):
        spaces = ""
        print(self.name)
        for card in self.stack:
            print(spaces, card)
            spaces += "  "
        return ""

def highPlay(mainDeck):
    play1 = deck.stack[0].rank
    print("You played:", deck.stack[0])
    play2 = deck.stack[1].rank
    print("Your opponent played:", deck.stack[1])
    if play1 > play2:
        return "play1"
    elif play2 > play1:
        return "play2"
    else:
        return "draw"

deck = cardStack()  #Making the main deck
deck.giveFullDeck()  #Making sure there's a full deck of cards
deck.shuffle(amount=5)  #Shuffling the deck
player1Hand = cardStack()  #Give Player stack
player2Hand = cardStack()  #Computer a stack
deck.splitDeckIntoTwoStacks(player1Hand, player2Hand) #Give half the deck to each player
round = 0


# Welcoming player to the game
print(" Welcome to the war!")
wait = input("press ENTER to start")

while True:
#Shuffle the players' deck at the start of each round
    player1Hand.shuffle()
    player2Hand.shuffle()
    wait = input("press ENTER to play a card")
    print()

    # loop for the rounds
    player1Hand.deal(1, deck)  # Deal one card into the deck
    player2Hand.deal(1, deck)  # Deal one card into the deck
    while True:
        highestPlay = highPlay(deck)
        #Give the cards to the winner
        if highestPlay == "play1":
            print("You won the round")
            deck.deal(len(deck.stack), player1Hand)
            break
        elif highestPlay == "play2":
            print("You lost the round")
            deck.deal(len(deck.stack), player2Hand)
            break

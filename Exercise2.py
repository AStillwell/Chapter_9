# Exercise2 Chapter 9
# Author: Alton Stillwell
# Date: 3/4/15
#######################
# One-Card War
# Each player will get a single card,
# player with highest value card wins
#######################
import cards, games
#######################
class CW_Card(cards.Card):
    ACE_VALUE = 1
    @property
    def value(self):
        v = CW_Card.RANKS.index(self.rank) + 1
        if v > 10:
            v = 10
        return v
#######################
class CW_Hand(cards.Hand):
    def __init__(self,name):
        super(CW_Hand,self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ":\t" + super(CW_Hand,self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == CW_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace:
            t = 11
        return t
#######################
class CW_Deck(cards.Deck):
    def populate(self):
        for suit in CW_Card.SUITS:
            for rank in CW_Card.RANKS:
                self.cards.append(CW_Card(rank,suit))
#######################
class CW_Player(CW_Hand):
    def lose(self):
        print(self.name,"loses.")
    def win(self):
        print(self.name,"wins.")
    def push(self):
        print(self.name,"pushes.")
####################
class CW_Game(object):
    def __init__(self,names):
        self.players = []
        for name in names:
            player = CW_Player(name)
            self.players.append(player)
        self.deck = CW_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def play(self):
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players:
            print(player)
        # finds top score
        topPlayerScore = 0
        for player in self.players:
            v = player.total
            if v > topPlayerScore:
                topPlayerScore = v
                topPlayer = player
        print("~~~~~~~~~~~~~~~")
        print(topPlayer,"is the winner!")
        print("With a final score of:",topPlayerScore)
        # resets the game
        for player in self.players:
            player.clear()
        self.deck = CW_Deck()
        self.deck.populate()
        self.deck.shuffle()
#######################
def main():
    print("\t\tWelcome to One-Card War!\n")
    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        while name == "":
            name = input("Enter different player name: ")
        names.append(name)
    print()
    game = CW_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")
#########################################
main()
input("Press <enter> to exit.")

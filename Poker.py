import random

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
 
    def print_card(self):
        lines = []
        lines.append("+---+")
        lines.append("|{}  |".format(self.suit))
        lines.append("| {} |".format(self.name))
        lines.append("|  {}|".format(self.suit))
        lines.append("+---+")
        return lines

class Deck:
    def __init__(self):
        self.cards = []
        self.cardsid = []
        self.reset()
 
    def reset(self):
        self.cards.clear()
        values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]
        ids = ["C", "S", "D", "H"]

        for i in range(len(values)):
            for suit in suits:
                self.cards.append(Card(names[i], suit, values[i]))
                self.cardsid.append(names + ids)
 
        self.shuffle()
 
    def shuffle(self):
        random.shuffle(self.cards)
 
    def draw(self):
        card = self.cards.pop()
        print(card)
        return card

class Player:
    def __init__(self):
        self.hand = []
        self.hand_id = []
    
    def draw_hand(self, deck):
        for _ in range(2):
            card = deck.draw()
            self.hand.append(card)
            self.hand_id.append(card.name + card.suit)

    def print_hand(self):
        card_lines = []
        for card in self.hand:
            card_lines.append(card.print_card())

        for i in range(len(card_lines[0])):
            line = ""
            for j in range(len(card_lines)):
                line += card_lines[j][i] + "  "
            print(line)

deck = Deck()
player = Player()
player.draw_hand(deck)
player.print_hand()
print(Player.hand_id)
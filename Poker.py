import random

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
        self.id = id
 
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
                self.cardsid.append(names[i] + ids[i % len(ids)])
 
        self.shuffle()
 
    def shuffle(self):
        random.shuffle(self.cards)
 
    def draw(self):
        card = self.cards.pop()
        print(card)
        return card

    def print_deck(self):
        for card in self.cards:
            for line in card.print_card():
                print(line)

class Player:
    def __init__(self):
        self.hand = []
        self.hand_id = []
    
    def draw_hand(self, deck):
        for _ in range(2):
            card = deck.draw()
            self.hand.append(card)
            self.hand_id.append(card.name + card.ids)

    def print_hand(self):
        card_lines = [[] for _ in range(5)]
        for card in self.hand:
            lines = card.print_card()
            for i, line in enumerate(lines):
                card_lines[i].extend(line)

        for line in card_lines:
            print("  ".join(line))
        print()

class Flop:
    def __init__(self, deck):
        self.cards = []
        for _ in range(3):
            card = deck.draw()
            self.cards.append(card)

    def print_flop(self):
        flop_lines = [[] for _ in range(5)]
        for card in self.cards:
            lines = card.print_card()
            for i, line in enumerate(lines):
                flop_lines[i].extend(line)

        for line in flop_lines:
            print("  ".join(line))
        print()

deck = Deck()
player = Player()
player.draw_hand(deck)
player.print_hand()
print(player.hand_id)

flop = Flop(deck)
flop.print_flop()

deck.print_deck()
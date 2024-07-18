import random

class Card:
    def __init__(self, number, suit, suitname, id):
        self.number = number
        self.suit = suit
        self.suitname = suitname
        self.id = id

    def print_card(self):
        lines = []
        lines.append("+---+")
        lines.append("|{}  |".format(self.suit))
        lines.append("| {} |".format(self.number))
        lines.append("|  {}|".format(self.suit))
        lines.append("+---+")
        return lines

class Deck:
    def __init__(self):
        self.cards = []
        self.cardsid = []
        self.cardsnames = []
        self.reset()
 
    def reset(self):
        self.cards.clear()
        numbers = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]
        suitnames = ["Spades", "Clubs", "Diamonds", "Hearts"]

        for number in numbers:
            for suit in suits:
                cardid =  str(number) + suitnames[suits.index(suit)].lower()[0] 
                card = Card(number, suit, suitnames[suits.index(suit)], cardid)
                self.cards.append(card)
                self.cardsnames.append(number + suitnames[suits.index(suit)])
                self.cardsid.append(cardid)

        self.shuffle()
 
    def shuffle(self):
        random.shuffle(self.cards)
 
    def draw(self):
        if len(self.cards) > 0:
            card = self.cards.pop()
            name = self.cardsnames.pop()
            card_id = self.cardsid.pop()
            return name, card_id, card
        else:
            return None

class Player:
    def __init__(self):
        self.hand = []
        self.hand_names = []
        self.hand_id = []
    
    def draw_hand(self, deck):
        for i in range(2):
            name, card_id, card = deck.draw()
            if card is not None:
                self.hand.append(card)
                self.hand_names.append(name)
                self.hand_id.append(card_id)

    def print_hand(self):
        for card in self.hand:
            lines = card.print_card()
            for line in lines:
                print(line)

class Flop:
    def __init__(self, deck):
        self.cards = []
        for _ in range(3):
            name, card_id, card = deck.draw()
            if card is not None:
                self.cards.append(card)

    def print_flop(self):
        for card in self.cards:
            lines = card.print_card()
            for line in lines:
                print(line)
            print()

deck = Deck()
player = Player()
player.draw_hand(deck)
player.print_hand()
print(player.hand_id)
flop = Flop(deck)

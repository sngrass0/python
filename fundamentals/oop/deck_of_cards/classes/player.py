from . import card
from . import deck
class Player:
    def __init__(self, hand):
        self.hand = hand
    
    def show_hand(self):
        for card in self.hand:
            card.card_info()
    
    def request_card(self, other_player):
        # TODO make it so that the player asks for
        # a random card in their deck everytime
        self.hand[0]
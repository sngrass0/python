from . import card
from . import deck
class Player:
    all_players = []

    def __init__(self, hand):
        self.hand = hand
        self.pairs = 0
        Player.all_players.append(self)
    
    def has_card(self, target):
        found_matches = []
        for card in self.hand:
            if card.string_val == target.string_val:
                found_matches.append(card)
        return found_matches
    
    def show_hand(self):
        for card in self.hand:
            card.card_info()
    
    @classmethod
    def all_players_hands(cls):
        for player in cls.all_players:
            print()
            player.show_hand()
    
    
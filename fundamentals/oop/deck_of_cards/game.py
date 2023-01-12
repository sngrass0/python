from classes.deck import Deck
from classes.player import Player

pool = Deck()
pool.shuffle_deck()
max_cards = 7

player_1 = Player(pool.draw_card(max_cards))
player_2 = Player(pool.draw_card(max_cards))

pool.cards_left()
Player.all_players_hands()

matches = player_2.has_card(player_1.hand[0])
if len(matches) > 0:
    print("found a match!")
else:
    print("go fish")

# making a go fish game
# [DONE] shuffle deck
# [DONE] give cards to players each player gets 7 cards
# [DONE] rest of the cards are put into an extra pool deck
# player1 asks player2 for a specific card
# if player2 has the requested card they will give all their copies to player1
# if player2 does NOT have the requested card player1 must "go fish"
# keep going until all pairs of four are found
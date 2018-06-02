from cards.card import Game


def play_game():
    game = Game()
    hands = game.deal(5, 2)
    players_hands = {'Raven': hands[0], 'Erin': hands[1]}
    print("Erin's hand: " + game.show_hand(players_hands['Erin']))
    print("Raven's hand: " + game.show_hand(players_hands['Raven']))
    print(game.check_win(players_hands))


play_game()

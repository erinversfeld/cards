import random


class Card:
    def __init__(self, rank, suite):
        self.suite = suite
        self.rank = rank


class Deck:
    suites = ['SPADES', 'CLUBS', 'DIAMONDS', 'HEARTS']
    ranks = [i for i in range(2, 11)]
    ranks.append(name for name in ['Ace', 'Jack', 'Queen', 'King'])

    def __init__(self):
        self.cards = []
        for suite in self.suites:
            for rank in self.ranks:
                card = Card(rank, suite)
                self.cards.append(card)
        self.num_cards = len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=1):
        hand = []
        for i in range(num_cards):
            hand.append(self.cards.pop(0))

        return hand


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def deal(self, num_cards, num_players):
        hands = []
        for i in range(num_players):
            hand = self.deck.deal(num_cards)
            hands.append(hand)
        return hands

    def check_win(self, players_hands):
        winning_condition = Card('SPADES', 5)
        for player in players_hands:
            if winning_condition in players_hands[player]:
                return 'Player %s wins!' % player
        return 'No one wins!'

    def show_hand(self, hand):
        card_str = '%s of %s'
        hand_str = card_str % (hand[0].rank, hand[0].suite)
        for card in hand[1:]:
            ', '.join(card_str % (card.rank, card.suite))
        return hand_str

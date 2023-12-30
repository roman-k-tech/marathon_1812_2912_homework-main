from __future__ import annotations
import random
import sys
from colorama import Fore, Back, Style


class Card:
    SUITS = '♠', '♡', '♢', '♣'
    RANKS = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.colour = Fore.RED if suit in ('♡', '♢') else None

    def __repr__(self):
        return f"{self.suit}{self.rank}"

    @property
    def value(self) -> int:

        """
        The value of a card is rank a number.
        """

        return self.RANKS.index(self.rank)

    @property
    def points(self) -> int:

        """
        Points this cart is worth
        """

        if self.suit == '♠' and self.rank == 'Q':
            return 13
        if self.suit == '♡':
            return 1
        return 0

    def __eq__(self, other: Card) -> bool:

        """
        equality check, returns True in case objects are equal, False if not
        """

        if type(other) is not self.__class__:
            return False

        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: Card) -> bool:

        """
        less than comparison, returns True in case first card has lower rank that second, False if not
        raises TypeError in case of uncomparable types
        """

        if type(other) is not self.__class__:
            raise TypeError('Uncomparable types: {} and {}'.format(self, other))

        return self.value < other.value

    def __str__(self):

        """
        generates card as coloured string
        """

        card_str = '{:3}'.format(self.suit + self.rank)
        if self.colour is not None:
            card_str = '{}{}{}'.format(self.colour, card_str, Style.RESET_ALL)

        return card_str


class Deck:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:

        """
        Create a new deck of 52 cards
        """

        deck = cls(cards=[Card(s, r) for r in Card.RANKS for s in Card.SUITS])
        if shuffle:
            deck.shuffle()

        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_hands: int) -> tuple[Deck]:

        """
        Deal the cards in the deck into num_hands.
        """

        cls = self.__class__
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):

        """
        Play a card from the player's hand.
        """

        card = self.hand.cards.pop(random.randrange(len(self.hand.cards)))

        print(f'{self.name}: {card}', end=' ')


class Game:
    PLAYERS = 'Player 1', 'Player 2', 'Player 3', 'Player 4'

    def __init__(self, *names: str) -> None:
        deck = Deck.create(shuffle=True)

        self.names = list(names + self.PLAYERS)[:4]

        self.hands = {n: Player(n, h) for n, h in zip(self.names, deck.deal(4))}

    def player_order(self, start=None):
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]

    def play(self) -> None:

        """
        Play a card game.
        """

        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)

        while self.hands[start_player].hand.cards:
            for name in turn_order:
                self.hands[name].play_card()
            print()


if __name__ == "__main__":
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()

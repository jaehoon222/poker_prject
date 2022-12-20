import poker
from pokereval.card import Card
from pokereval import hand_evaluator


def cardToString(card):
    # suit
    card = list(card)
    if card[1] == "♠":
        card[1] = "s"
    elif card[1] == "♥":
        card[1] = "h"
    elif card[1] == "♣":
        card[1] = "c"
    elif card[1] == "♦":
        card[1] = "d"

    # rank
    if card[0] == "T":
        card[0] = 10
    elif card[0] == "J":
        card[0] = 11
    elif card[0] == "Q":
        card[0] = 12
    elif card[0] == "K":
        card[0] = 13
    elif card[0] == "A":
        card[0] = 14
    else:
        card[0] = int(card[0])

    return card


def make_random_hand(deck):
    card1 = cardToString(str(deck.pop()))
    card2 = cardToString(str(deck.pop()))

    hand = [Card(card1[0], card1[1]), Card(
        card2[0], card2[1])]

    return hand


def make_random_flop(deck):
    card1 = cardToString(str(deck.pop()))
    card2 = cardToString(str(deck.pop()))
    card3 = cardToString(str(deck.pop()))

    flop = [Card(card1[0], card1[1]), Card(
        card2[0], card2[1]), Card(card3[0], card3[1])]

    return flop


def make_random_turn_rever(deck):
    card1 = cardToString(str(deck.pop()))

    card = [Card(card1[0], card1[1])]

    return card
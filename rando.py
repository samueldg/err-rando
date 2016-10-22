import random

from errbot import botcmd
from errbot import BotPlugin


CARD_VALUES = [
    'ace',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'jack',
    'queen',
    'king',
]
CARD_VALUES_NUM = [
    'A',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
]
CARD_SUITS = [
  'hearts',
  'diamonds',
  'clubs',
  'spades',
]
CARD_SUITS_SYMBOLS = [
    u'\u2665',  #heart
    u'\u2666',  #diamonds
    u'\u2663',  #clubs
    u'\u2660',  #spades
]


class Rando(BotPlugin):

    @botcmd(admin_only=False)
    def cointoss(self, mess, args):
        """Returns heads or tails"""
        return random.choice(['heads', 'tails'])

    @botcmd(admin_only=False)
    def diceroll(self, mess, args):
        """Returns a dice number (1 through 6)"""
        return random.randint(1, 6)

    @botcmd(admin_only=False)
    def dealcard(self, mess, args):
        """Returns a card: [ace..king] of [hearts|diamonds|clubs|spades]"""
        value = random.choice(zip(CARD_VALUES, CARD_VALUES_NUM))
        suit = random.choice(zip(CARD_SUITS, CARD_SUITS_SYMBOLS))
        return u"{0} of {1} [{2}{3}]".format(value[0], suit[0], suit[1], value[1])

    @botcmd(split_args_with=' ', admin_only=False)
    def pick(self, mess, args):
        """ Returns one of the user-provided choices"""
        return random.choice(args)

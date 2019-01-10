import random
import re

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
    '\u2665',  # hearts
    '\u2666',  # diamonds
    '\u2663',  # clubs
    '\u2660',  # spades
]

# See https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
EIGHTBALL_ANSWERS = [
    # Affirmative
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",

    # Non-committal
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",

    # Negative
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

_DICEROLLS = re.compile("(\d*)[wW](\d+)")

class Rando(BotPlugin):

    @botcmd(admin_only=False)
    def cointoss(self, mess, args):
        """Returns heads or tails"""
        return random.choice(['heads', 'tails'])

    @botcmd(admin_only=False)
    def diceroll(self, mess, args):
        """Returns a 6-sided dice roll. Optional argument like '3w6 1w12'."""
        if not args:
            return random.randint(1, 6)
        total = 0
        rolls = list()
        for d in re.finditer(_DICEROLLS, args):
            if not d.group(1):
                count = 1
            else:
                count = int(d.group(1))
            sides = int(d.group(2))
            if count > 100:
                return "Sry, I don't have that many w%d in my bag" % sides
            if sides > 100:
                return "Sry, I have no w%d in my bag" % sides
            if sides == 0:
                continue
            for i in range(count):
                roll = random.randint(1, sides)
                total += roll
                rolls.append(roll)
        if not rolls:
            return
        elif len(rolls) == 1:
            return '%d' % total
        else:
            srolls = ', '.join(map(str, rolls))
            return '%d  (%s)' % (total, srolls)

    @botcmd(admin_only=False)
    def dealcard(self, mess, args):
        """Returns a card: [ace..king] of [hearts|diamonds|clubs|spades]"""
        value = random.choice(list(zip(CARD_VALUES, CARD_VALUES_NUM)))
        suit = random.choice(list(zip(CARD_SUITS, CARD_SUITS_SYMBOLS)))
        return "{0} of {1} [{2}{3}]".format(value[0], suit[0], suit[1], value[1])

    @botcmd(split_args_with=' ', admin_only=False)
    def pick(self, mess, args):
        """Returns one of the user-provided choices"""
        return random.choice(args)

    @botcmd(name='8ball')
    def eightball(self, mess, args):
        """Returns a Magic 8-Ball reply"""
        return random.choice(EIGHTBALL_ANSWERS)

    @botcmd(split_args_with=' ', admin_only=False)
    def shuffle(self, mess, args):
        """Returns arguments in random order"""
        random.shuffle(args)
        return ' '.join(args)

import random

from errbot import botcmd
from errbot import BotPlugin

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
        value = random.choice([('two', '2'), ('three', '3'), ('four', '4'),
                               ('five', '5'), ('six', '6'), ('seven', '7'),
                               ('eight', '8'), ('nine', '9'), ('ten', '10'),
                               ('jack', 'J'), ('queen', 'Q'), ('king', 'K'),
                               ('ace', 'A')])
        suit = random.choice([('hearts', u'\u2665'),
                              ('diamonds', u'\u2666'),
                              ('clubs', u'\u2663'),
                              ('spades', u'\u2660')])
        return u"{0} of {1} [{2}{3}]".format(value[0], suit[0], suit[1], value[1])

    @botcmd(split_args_with=' ', admin_only=False)
    def pick(self, mess, args):
        """ Returns one of the user-provided choices"""
        return random.choice(args)

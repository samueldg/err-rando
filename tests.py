"""Basic output validation tests"""
from __future__ import unicode_literals

import re
import sys
import unittest

from rando import CARD_SUITS
from rando import CARD_SUITS_SYMBOLS
from rando import CARD_VALUES
from rando import CARD_VALUES_NUM
from rando import Rando


def choice_pattern(choices):
    """Utility method to return the regex pattern for a choice of strings

    >>> choice_pattern(['foo', 'bar'])
    '(foo|bar)'

    """
    return r'({0})'.format('|'.join(choices))

class RandoBotTest(unittest.TestCase):

    def setUp(self):
        self.bot = Rando(bot=None)

    def test_cointoss(self):
        expected_results = ['heads', 'tails']
        result = self.bot.cointoss(None, None)
        self.assertIn(result, expected_results)

    def test_diceroll(self):
        expected_results = [1, 2, 3, 4, 5, 6]
        result = self.bot.diceroll(None, None)
        self.assertIn(result, expected_results)

    def test_dealcard(self):
        suits_pattern = choice_pattern(CARD_SUITS)
        values_pattern = choice_pattern(CARD_VALUES)
        suit_symbols_pattern = choice_pattern(CARD_SUITS_SYMBOLS)
        values_num_pattern = choice_pattern(CARD_VALUES_NUM)

        card_pattern = r'{0} of {1} \[{2}{3}\]'.format(values_pattern,
                                                    suits_pattern,
                                                    suit_symbols_pattern,
                                                    values_num_pattern)
        card_pattern = re.compile(card_pattern, re.UNICODE)

        result = self.bot.dealcard(None, None)
        self.assertTrue(re.match(card_pattern, result))

    def test_pick(self):
        choices = ['Athos', 'Aramis', 'Porthos', 'D\'Artagnan']
        result = self.bot.pick(None, args=choices)
        self.assertIn(result, choices)

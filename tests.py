"""Basic output validation tests"""
import re

import rando

from rando import CARD_SUITS
from rando import CARD_SUITS_SYMBOLS
from rando import CARD_VALUES
from rando import CARD_VALUES_NUM


# pytest
extra_plugin_dir = '.'
pytest_plugins = ['errbot.backends.test']


def choice_pattern(choices):
    """Utility method to return the regex pattern for a choice of strings

    >>> choice_pattern(['foo', 'bar'])
    '(foo|bar)'

    """
    return r'({0})'.format('|'.join(choices))


def test_cointoss(testbot):
    expected_results = ['heads', 'tails']
    testbot.push_message('!cointoss')
    result = testbot.pop_message()
    assert result in expected_results


def test_diceroll(testbot):
    expected_results = [str(num) for num in range(1, 7)]
    testbot.push_message('!diceroll')
    result = testbot.pop_message()
    assert result in expected_results


def test_dealcard(testbot):
    suits_pattern = choice_pattern(CARD_SUITS)
    values_pattern = choice_pattern(CARD_VALUES)
    suit_symbols_pattern = choice_pattern(CARD_SUITS_SYMBOLS)
    values_num_pattern = choice_pattern(CARD_VALUES_NUM)

    card_pattern = r'{0} of {1} \[{2}{3}\]'.format(values_pattern,
                                                suits_pattern,
                                                suit_symbols_pattern,
                                                values_num_pattern)
    card_pattern = re.compile(card_pattern, re.UNICODE)

    testbot.push_message('!dealcard')
    result = testbot.pop_message()
    assert re.match(card_pattern, result)


def test_pick(testbot):
    choices = ['Athos', 'Aramis', 'Porthos', 'D\'Artagnan']
    choices_string = ' '.join(choices)
    testbot.push_message('!pick ' + choices_string)
    result = testbot.pop_message()
    assert result in choices

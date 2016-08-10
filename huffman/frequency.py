from collections import Counter
from re import finditer


def char_frequency(text):
    """Return frequency of each character in a given text file"""

    return dict(Counter(text))


def code_frequency(file):
    """Return frequency of each character or word in a given text file"""
    with open(file) as f:
        for i in finditer(r'([a-zA-Z][a-zA-Z0-9]*)|(.+)', f.read()):
            pass

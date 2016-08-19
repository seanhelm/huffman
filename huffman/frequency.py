from collections import Counter


def char_frequency(text):
    """Return frequency of each character in a given text file"""

    return dict(Counter(text))

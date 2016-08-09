from collections import Counter
from re import finditer


def char_frequency(file):
    with open(file) as f:
        return dict(Counter(f.read()))


def code_frequency(file):
    with open(file) as f:
        for i in finditer(r'([a-zA-Z][a-zA-Z0-9]*)|(.+)', f.read()):
            pass

from huffman.frequency import char_frequency
from bisect import insort_left
from functools import total_ordering
from heapq import heappop, heapify


@total_ordering
class Node:
    """Individual node for the huffman tree"""

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

        self.left = None
        self.right = None
        self.parent = None

    def __len__(self):
        return self.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return str(self.char) + ': ' + str(self.freq)


class Tree:
    """Huffman tree to hold character nodes for encoding/decoding"""

    def __init__(self, file):
        with open(file) as f:
            self.text = f.read()

        data = char_frequency(self.text)
        nodes = self.dict_to_nodes(data)
        heapify(nodes)
        self.mapping = dict([(n.char, n) for n in nodes])
        self.compress(nodes)
        self.head = nodes[0]

    @staticmethod
    def dict_to_nodes(data):
        return sorted([Node(k, v) for k, v in data.items()])

    @staticmethod
    def compress(nodes):
        while len(nodes) > 1:
            first_node, second_node = heappop(nodes), heappop(nodes)

            parent = Node(None, first_node.freq + second_node.freq)
            parent.right, parent.left = second_node, first_node
            first_node.parent = second_node.parent = parent
            insort_left(nodes, parent)

    def decode(self, code):
        current = self.head
        text = ''

        for char in code:
            if char == '0':
                current = current.left
            elif char == '1':
                current = current.right

            if not current.left and not current.right:
                text += current.char
                current = self.head

        return text

    def encode(self):
        encoding = ''

        for char in self.text:
            current = self.mapping[char]
            char_encoding = ''

            while current.parent:
                if current.parent.left == current:
                    char_encoding = '0' + char_encoding
                elif current.parent.right == current:
                    char_encoding = '1' + char_encoding
                current = current.parent

            encoding += char_encoding

        return encoding

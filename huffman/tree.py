from bisect import insort_left
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __len__(self):
        return self.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __str__(self):
        return str(self.char) + ': ' + str(self.freq)


class Tree:
    def __init__(self, data):
        nodes = self.dict_to_nodes(data)
        self.compress(nodes)
        self.head = nodes[0]

    @staticmethod
    def dict_to_nodes(data):
        return sorted([Node(k, v) for k, v in data.items()])

    @staticmethod
    def compress(nodes):
        while len(nodes) > 1:
            first_node, second_node = nodes.pop(0), nodes.pop(0)
            parent = Node(None, first_node.freq + second_node.freq)
            parent.right, parent.left = second_node, first_node
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

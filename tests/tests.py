import unittest

from huffman.tree import Node, Tree
from huffman.frequency import char_frequency, code_frequency


class MyTestCase(unittest.TestCase):
    tree = Tree({'1': 5, '2': 7, '3': 10, '4': 15, '5': 20, '6': 45})

    def test_char_freq(self):
        self.assertEqual({'a': 3, 'b': 3, 'c': 8, 'd': 4, 'e': 2}, char_frequency('tests/test.txt'))

    def test_node(self):
        node = Node('c', 50)
        self.assertEqual('c', node.char)
        self.assertEqual(50, node.freq)
        self.assertEqual('c: 50', str(node))

    def test_init(self):
        self.assertEqual(102, self.tree.head.freq)
        self.assertEqual(45, self.tree.head.left.freq)
        self.assertEqual('6', self.tree.head.left.char)

    def test_decode(self):
        self.assertEqual('631245', self.tree.decode('010010101011110111'))


if __name__ == '__main__':
    unittest.main()

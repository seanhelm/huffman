import unittest

from huffman.tree import Node, Tree


class MyTestCase(unittest.TestCase):

    def test_node(self):
        node = Node('c', 50)
        self.assertEqual('c', node.char)
        self.assertEqual(50, node.freq)
        self.assertEqual('c: 50', str(node))

    def test_init(self):
        tree = Tree('tests/tree_test.txt')
        self.assertEqual(102, tree.head.freq)
        self.assertEqual(45, tree.head.left.freq)
        self.assertEqual('6', tree.head.left.char)

    def test_decode(self):
        tree = Tree('tests/tree_test.txt')
        self.assertEqual('631245', tree.decode('010010101011110111'))

    def test_encode(self):
        tree = Tree('tests/encode_test.txt')
        self.assertEqual('111000101', tree.encode())

if __name__ == '__main__':
    unittest.main()

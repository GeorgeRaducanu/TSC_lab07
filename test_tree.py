import unittest
from tree import *

class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.node1 = Node(5)
        self.tree = Tree()
        self.node2 = Node(3)
        self.node3 = Node(7)
        self.node1.left = self.node2
        self.node1.right = self.node3
    
    def test_find(self):
        self.assertEqual(self.tree._find(5, self.node1), self.node1)

    def test_find1(self):
        self.assertNotEqual(self.tree._find(2, self.node1), self.node1)


if __name__ == '__main__':
    unittest.main()
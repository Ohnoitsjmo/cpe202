# Justin Mo
from bst import *
import unittest

class Tests(unittest.TestCase):
    def test_prefix_iterator(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 7
        bst1.root = Node(10, Node(5, Node(1, None, None), Node(7, None, None)), Node(12, Node(11, None, None), Node(15, None, None)))
        i = prefix_iterator(bst1)
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
    def test_infix_iterator(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 7
        bst1.root = Node(10, Node(5, Node(1, None, None), Node(7, None, None)), Node(12, Node(11, None, None), Node(15, None, None)))  
        i = infix_iterator(bst1)
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
    def test_postfix_iterator(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 7
        bst1.root = Node(10, Node(5, Node(1, None, None), Node(7, None, None)), Node(12, Node(11, None, None), Node(15, None, None)))  
        i = postfix_iterator(bst1)
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))

    def test_comes_before(self):
        self.assertTrue(comes_before(3, 5))
        self.assertFalse(comes_before(5, 3))
    
    def test_repr(self):
        self.assertEqual(repr(Node(1, 2, 3)), str("Node(Parent: 1, Left: 2, Right: 3)"))
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 1
        bst1.root = Node(1, None, None)
        self.assertEqual(repr(bst1), str("Node: Node(Parent: 1, Left: None, Right: None), Size: 1"))

    def test_is_empty(self):
        bst1 = None
        bst2 = BinarySearchTree(comes_before)
        bst2.root = Node(3, None, None)
        bst2.size = 1
        bst3 = BinarySearchTree(comes_before)
        bst3.root = None
        bst3.size = 0
        self.assertTrue(is_empty(bst3))
        self.assertTrue(is_empty(bst1))
        self.assertFalse(is_empty(bst2))

    def test_insert(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 7
        bst1.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, None)))
        bst2 = BinarySearchTree(comes_before)
        bst2.size = 8
        bst2.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, Node(9, None, None))))
        bst3 = BinarySearchTree(comes_before)
        bst3.size = 0
        bst3.root = None
        bst4 = BinarySearchTree(comes_before)
        bst4.size = 1
        bst4.root = Node(3, None, None)
        bst1.root = insert(bst1, 9)
        bst3.root = insert(bst3, 3)
        bst7 = BinarySearchTree(comes_before)
        bst7.size = 7
        bst7.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, Node(9, None, None))))
        bst7.root = insert(bst7, 1)
        bst8 = BinarySearchTree(comes_before)
        bst8.size = 8
        bst8.root =  Node(5, Node(3, Node(2, Node(1, None, None), None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, Node(9, None, None))))
        #self.assertEqual(bst5, bst6)
        self.assertEqual(bst1, bst2)
        self.assertEqual(bst7, bst8)

    def test_lookup(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 7
        bst1.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, None)))
        bst2 = BinarySearchTree(comes_before)
        bst2.size = 7
        bst2.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, None)))
        self.assertTrue(lookup(bst1, 3))
        self.assertFalse(lookup(bst2, 11))
        bst3 = BinarySearchTree(comes_before)
        bst3.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, Node(9, None, None))))
        bst3.size = 8
        self.assertTrue(lookup(bst3, 9))

    def test_delete(self):
        bst1 = BinarySearchTree(comes_before)
        bst1.size = 1
        bst1.root = Node(3, None, None)
        bst2 = BinarySearchTree(comes_before)
        bst2.size = 0
        bst2.root = None
        bst1.root = delete(bst1, 3)
        bst3 = BinarySearchTree(comes_before)
        bst3.size = 8
        bst3.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, Node(9, None, None)))) 
        bst4 = BinarySearchTree(comes_before)
        bst4.size = 7
        bst4.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, None)))
        bst3.root = delete(bst3, 9)
        bst5 = BinarySearchTree(comes_before)
        bst5.size = 8
        bst5.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(9, Node(8, None, None), None)))
        bst5.root = delete(bst5, 8)  
        bst6 = BinarySearchTree(comes_before)
        bst6.size = 8
        bst6.root = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, Node(6, None, None), Node(8, None, None)))
        bst6.root = delete(bst6, 5)
        bst7 = BinarySearchTree(comes_before)
        bst7.size = 7
        bst7.root = Node(6, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, Node(8, None, None)))
        bst8 = BinarySearchTree(comes_before)
        bst8.size = 8
        bst8.root = Node(10, Node(5, None, None), Node(18, Node(15, Node(13, None, None), Node(17, None, None)), Node(18, None, None))) 
        
        #bst8.root = delete(bst8, 18)
        bst9 = BinarySearchTree(comes_before)
        bst9.size = 7 
        bst9.root = Node(10, Node(5, None, None), Node(13, Node(15, None, Node(17, None, None)), Node(18, None, None))) 
        bst10 = BinarySearchTree(comes_before)
        bst10.size = 7
        bst10.root = Node(10, None, Node(15, Node(14, Node(13, None, None), None), Node(20, Node(18, None, None), Node(25, None, None))))
        bst10.root = delete(bst10, 15)
        bst11 = BinarySearchTree(comes_before)
        bst11.size = 6
        bst11.root = Node(10, None, Node(18, Node(14, Node(13, None, None), None), Node(20, None, Node(25, None, None))))
        bst69 = BinarySearchTree(comes_before)
        bst69.size = 0
        bst69.root = Node(1, None, None)
        bst69.root = delete(bst69, 2)
        bst70 = BinarySearchTree(comes_before)
        bst70.size = 0
        bst70.root = Node(1, None, None)
        bst71 = BinarySearchTree(comes_before)
        bst71.size = 7
        bst71.root = Node(10, None, Node(15, Node(14, Node(13, None, None), None), Node(20, Node(18, Node(17, None, None), None), Node(25, None, None))))
        
        bst72 = BinarySearchTree(comes_before)
        bst72.size = 2
        bst72.root = Node(5, Node(3, None, None), None)
        bst72.root = delete(bst72, 5)
        bst73 = BinarySearchTree(comes_before)
        bst73.size = 1
        bst73.root = Node(3, None, None)
        bst74 = BinarySearchTree(comes_before)
        bst74.size = 2
        bst74.root = Node(5, None, Node(3, None, None))
        bst74.root = delete(bst74, 5)
        self.assertEqual(bst74, bst73)
        self.assertEqual(bst72, bst73)
        self.assertEqual(bst69, bst70)
        self.assertEqual(bst10, bst11)
        #self.assertEqual(bst8, bst9)
        self.assertEqual(bst6, bst7)
        self.assertEqual(bst3, bst4)
        self.assertEqual(bst1, bst2)

if __name__ == '__main__':
    unittest.main()

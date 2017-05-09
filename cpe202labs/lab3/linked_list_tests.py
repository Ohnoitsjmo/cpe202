import unittest
from linked_list import *

class TestList(unittest.TestCase):
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    def test_repr(self):
        self.assertEqual(repr(Pair(3, "mt")), str(Pair(3, "mt")))
    def test_empty(self):
        self.assertEqual(empty_list(), None)
    def test_length(self):
        self.assertEqual(length(Pair(4, Pair(3, None))), 2)
        self.assertEqual(length(None), 0)
    def test_add(self):
        self.assertEqual(add(Pair(1, Pair(3, None)), 1, 2), Pair(1, Pair(2, Pair(3, None))))
        self.assertEqual(add(Pair(3, None), 0, 9), Pair(9, Pair(3, None)))
        with self.assertRaises(IndexError):
            add(Pair(3, None), 5, 9)
        self.assertEqual(add(Pair(3, None), 1, 9), Pair(3, Pair(9, None)))
        self.assertEqual(add(None, 0, 5), Pair(5, None))
    def test_get(self):
        self.assertEqual(get(Pair(3, None), 0), 3)
        self.assertEqual(get(Pair(3, Pair(4, None)), 1), 4)
        with self.assertRaises(IndexError):
            get(Pair(3, None), 5)
    def test_set(self):
        with self.assertRaises(IndexError):
            set(None, 4, 5), Pair(5, None)
        self.assertEqual(set(Pair(2, None), 0, 5), Pair(5, None))
        self.assertEqual(set(Pair(2, Pair(3, Pair(5, None))), 1, 5), Pair(2, Pair(5, Pair(5, None))))
        self.assertEqual(set(Pair(2, Pair(3, None)), 1, 5), Pair(2, Pair(5, None)))
    def test_remove(self):
        with self.assertRaises(IndexError):
            remove(Pair(1, None), 5)
        self.assertEqual(remove(Pair(1, Pair(2, None)), 0), (1, Pair(2, None)))
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 1), (2, Pair(1, Pair(3, None))))
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 0), (1, Pair(2, Pair(3, None))))
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
        with self.assertRaises(IndexError):
            remove(None, 1)
    def test_remove_helper(self):
        self.assertEqual(remove_helper(Pair(1, Pair(2, None)), 0), 1)
        with self.assertRaises(IndexError):
            remove_helper(None, 2)
        with self.assertRaises(IndexError):
            remove_helper(Pair(1, Pair(2, None)), 3)
    def test_remove_helper2(self):
        with self.assertRaises(IndexError):
            remove_helper2(None, 2)
        with self.assertRaises(IndexError):
            remove_helper2(Pair(1, Pair(2, None)), 3)
if __name__ == '__main__':
    unittest.main()

import unittest
from array_list import *

class TestList(unittest.TestCase):
    def test_repr(self):
        list1 = List()
        list1.array = [1, 2, 3, 4, 5]
        list1.length = 5
        list1.capacity = 10
        self.assertEqual(repr(list1), "1, 2, 3, 4, 5")

    def test_eq(self):
        list1 = List()
        list2 = List()
        list1.array = [1, 2, 3, 5, 7]
        list1.length = 5
        list1.capacity = 10
        list2.array = [1, 2, 3, 4, 8]
        list2.length = 5
        list1.capacity = 10
        self.assertFalse(list1 == list2)
    
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty(self):
        list1 = empty_list() 
        list1.length = 5 
        list1.capacity = 15 
        list2 = empty_list() 
        list3 = empty_list()
        self.assertEqual(list1.length, 5)
        self.assertEqual(list1.capacity, 15) 
        self.assertEqual(list2, list3) 

    def test_length(self):
        list1 = List()
        list1.length = 5
        self.assertEqual(length(list1), 5)
        self.assertEqual(length(None), 0)

    def test_get(self):
        list1 = List()
        list1.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 10
        self.assertEqual(get(list1, 1), 2)
        list3 = List()
        list3.array = [1, 2, 3]
        list3.length = 3
        list4 = List()
        list4.array = [9, 2, 5]
        list4.length = 2
        with self.assertRaises(IndexError):
            get(list3, 5) 
        with self.assertRaises(IndexError):
            get(list3, -1)
        with self.assertRaises(IndexError):
            get(empty_list(), 0)
        self.assertRaises(IndexError, get, list4, 2)
        list5 = List()
        list5.length = 5
        list5.capacity = 6
        list5.array = [None, None, None, 5]

    def test_add(self):
        list1 = List()
        list1.array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 9
        list1.capacity = 10
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 10
        list3 = List()
        list3.array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list3.length = 11
        list3.capacity = 20
        list4 = List()
        list4.array = [1, 2, 3, 4]
        list4.length = 4
        list4.capacity = 10
        list5 = List()
        list5.array = [1, 2, 3, 4, 5]
        list5.length = 5
        list5.capacity = 10
        self.assertEqual(add(list1, 1, 2), list2)
        self.assertEqual(add(list2, 0, 0), list3) 
        self.assertEqual(add(list4, 4, 5), list4)
        with self.assertRaises(IndexError):
            add(list1, 100, 1)
        list6 = List()
        list6.array = [12, 4, 5]
        list6.length = 2
        list6.capcity = 10
        self.assertEqual((add(add(empty_list(), 0, 12), 1, 4)), list6)
        self.assertRaises(IndexError, set, list6, 2, 5)
        self.assertRaises(IndexError, set, List(), 1, 12)

    def test_set(self):
        list1 = List()
        list1.array = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 10
        list1.capacity = 10
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 10
        self.assertEqual(set(list1, 1, 2), list2)
        with self.assertRaises(IndexError):
            set(list1, -2, 1)
        with self.assertRaises(IndexError):
            set(list1, 11, 1)

    def test_remove(self):
        list1 = List()
        list1.array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 11
        list1.capacity = 20
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 20
        list3 = List()
        list3.array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
        list3.length = 9
        list3.capacity = 20
        self.assertEqual(remove(list1, 0), (0, list2))
        self.assertEqual(remove(list2, 1), (2, list3))
        with self.assertRaises(IndexError):
            remove(list1, 100)

if __name__ == '__main__':
    unittest.main()

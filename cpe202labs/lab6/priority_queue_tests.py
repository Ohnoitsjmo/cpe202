# Justin Mo
import unittest
from priority_queue import *
class TestPqueue(unittest.TestCase):
    def test_comes_before(self):
        self.assertTrue(comes_before(1, 2))

    def test_repr(self):
        queue = empty_pqueue(comes_before)
        queue.size = 3
        queue.head = [None, 1, 2, 3]
        self.assertEqual(repr(queue), "Queue: [None, 1, 2, 3]")

    def test_empty_pqueue(self):
        self.assertEqual(empty_pqueue(comes_before), PriorityQueue(comes_before))

    def test_enqueue(self):
        pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 0
        pqueue1.head = [None]
        pqueue2 = empty_pqueue(comes_before)
        pqueue2.size = 1
        pqueue2.head = [None, 1]
        pqueue3 = empty_pqueue(comes_before)
        pqueue3.size = 6 
        pqueue3.head = [None, 1, 3, 4, 5, 6, 7] 
        pqueue4 = empty_pqueue(comes_before)
        pqueue4.size = 7
        pqueue4.head = [None, 1, 3, 2, 5, 6, 7, 4]
        pqueue5 = empty_pqueue(comes_before)
        pqueue5.size = 7
        pqueue5.head = [None, 1, 2, 4, 5, 6, 7, 8]
        pqueue6 = empty_pqueue(comes_before)
        pqueue6.size = 8
        pqueue6.head = [None, 1, 2, 4, 3, 6, 7, 8, 5]
        pqueue7 = empty_pqueue(comes_before)
        pqueue7.size = 7
        pqueue7.head = [None, 1, 3, 4, 5, 6, 7, 8]
        pqueue8 = empty_pqueue(comes_before)
        pqueue8.size = 8
        pqueue8.head = [None, 1, 2, 4, 3, 6, 7, 8, 5]
        pqueue9 = empty_pqueue(comes_before)
        pqueue9.size = 7
        pqueue9.head = [None, 1, 2, 3, 4, 5, 6, 7]
        pqueue10 = empty_pqueue(comes_before)
        pqueue10.size = 8
        pqueue10.head = [None, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(enqueue(pqueue9, 8), pqueue10)
        self.assertEqual(enqueue(pqueue7, 2), pqueue8)
        self.assertEqual(enqueue(pqueue5, 3), pqueue6)
        self.assertEqual(enqueue(pqueue3, 2), pqueue4)
        self.assertEqual(enqueue(pqueue1, 1), pqueue2)
        
    def test_dequeue(self):
        pqueue = empty_pqueue(comes_before)
        with self.assertRaises(IndexError):
            dequeue(pqueue)
        pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 1
        pqueue1.head = [None, 1]
        pqueue2 = empty_pqueue(comes_before)
        pqueue2.size = 0
        pqueue2.head = [None]
        pqueue3 = empty_pqueue(comes_before)
        pqueue3.size = 7
        pqueue3.head = [None, 1, 2, 3, 4, 5, 6, 7]
        pqueue4 = empty_pqueue(comes_before)
        pqueue4.size = 6
        pqueue4.head = [None, 2, 4, 3, 7, 5, 6]
        pqueue5 = empty_pqueue(comes_before)
        pqueue5.size = 7
        pqueue5.head = [None, 1, 3, 2, 4, 5, 6, 7]
        pqueue6 = empty_pqueue(comes_before)
        pqueue6.size = 6
        pqueue6.head = [None, 2, 3, 6, 4, 5, 7]
        pqueue7 = empty_pqueue(comes_before)
        pqueue7.size = 5
        pqueue7.head = [None, 1, 2, 3, 5, 4]
        pqueue8 = empty_pqueue(comes_before)
        pqueue8.size = 4
        pqueue8.head = [None, 2, 4, 3, 5]
        self.assertEqual(dequeue(pqueue7), (1, pqueue8))
        self.assertEqual(dequeue(pqueue5), (1, pqueue6))
        self.assertEqual(dequeue(pqueue3), (1, pqueue4))
        self.assertEqual(dequeue(pqueue1), (1, pqueue2))


    def test_peek(self):
        pqueue = empty_pqueue(comes_before)
        with self.assertRaises(IndexError):
            peek(pqueue)
        pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 3
        pqueue1.head = [None, 1, 2, 3]
        self.assertEqual(peek(pqueue1), 1)

    def test_size(self):
        pqueue = empty_pqueue(comes_before)
        self.assertEqual(size(pqueue), 0)
        pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 3
        pqueue1.head = [None, 1, 2, 3]
        self.assertEqual(size(pqueue1), 3)

    def test_is_empty(self):
        pqueue = empty_pqueue(comes_before)
        self.assertTrue(is_empty(pqueue))
        pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 3
        pqueue1.head = [None, 1, 2, 3]
        self.assertFalse(is_empty(pqueue1))

'''pqueue1 = empty_pqueue(comes_before)
        pqueue1.size = 0
        pqueue1.head = [None]
        pqueue3 = empty_pqueue(comes_before)
        pqueue3.size = 1
        pqueue3.head = [1] 
        pqueue2 = empty_pqueue(comes_before)
        pqueue2.size = 2
        pqueue2.head = [1, 3]
        pqueue4 = empty_pqueue(comes_before)
        pqueue4.size = 3
        pqueue4.head = [1, 2, 3]
        pqueue5 = empty_pqueue(comes_before)
        pqueue5.size = 3
        pqueue5.head = [1, 2, 3]
        pqueue6 = empty_pqueue(comes_before)
        pqueue6.size = 4
        pqueue6.head = [1, 2, 3, 4] 
        pqueue7 = empty_pqueue(comes_before)
        pqueue7.size = 5
        pqueue7.head = [1, 3, 4, 5, 6]
        pqueue8 = empty_pqueue(comes_before)
        pqueue8.size = 6
        pqueue8.head = [1, 2, 3, 4, 5, 6]
        pqueue9 = empty_pqueue(comes_before)
        pqueue9.size = 5
        pqueue9.head = [1, 2, 3, 4, 5]
        pqueue10 = empty_pqueue(comes_before)
        pqueue10.size = 6
        pqueue10.head = [1, 2, 3, 4, 5, 6]
        self.assertEqual(enqueue(pqueue9, 6), pqueue10)
        self.assertEqual(enqueue(pqueue7, 2), pqueue8)
        self.assertEqual(enqueue(pqueue1, 1), pqueue3)
        self.assertEqual(enqueue(pqueue2, 2), pqueue4)
        self.assertEqual(enqueue(pqueue5, 4), pqueue6)'''

if __name__ == "__main__":
    unittest.main()








import unittest
from list_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_repr(self):
        queue = Queue()
        queue.size = 1
        queue.head = Pair(1, None)
        self.assertEqual(repr(queue), "Queue: Pair(1, None)")
    def test_empty(self):
        self.assertEqual(empty_queue(), Queue())

    def test_enqueue(self):
        queue1 = Queue()
        queue2 = Queue()
        queue2.size = 1
        queue2.head = Pair(1, None)
        self.assertEqual(enqueue(queue1, 1), queue2)
        queue3 = Queue()
        queue3.size = 1
        queue3.head = Pair(1, None)
        queue4 = Queue()
        queue4.size = 2
        queue4.head = Pair(1, Pair(2, None))
        self.assertEqual(enqueue(queue3, 2), queue4)

    def test_dequeue(self):
        queue1 = Queue()
        queue1.size = 3
        queue1.head = Pair(1, Pair(2, Pair(3, None)))
        queue2 = Queue()
        queue2.size = 2
        queue2.head = Pair(2, Pair(1, None))
        self.assertEqual(dequeue(queue1), (3, queue2))
        queue3 = Queue()
        with self.assertRaises(IndexError):
            dequeue(queue3)

    def test_peek(self):
        queue1 = Queue()
        with self.assertRaises(IndexError):
            peek(queue1)
        queue2 = Queue()
        queue2.size = 3
        queue2.head = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(peek(queue2), 1)

    def test_size(self):
        queue1 = Queue()
        queue1.size = 2
        queue1.head = Pair(1, Pair(2, None))
        self.assertEqual(size(queue1), 2)

    def test_is_empty(self):
        queue1 = Queue()
        self.assertTrue(is_empty(queue1))
        queue2 = Queue()
        queue2.size = 1
        queue2.head = Pair(1, None)
        self.assertFalse(is_empty(queue2))

if __name__ == "__main__":
    unittest.main()

import unittest
from circular_queue import *

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
        queue.front = 0
        queue.back = 2
        queue.head = [1, 2] 
        self.assertEqual(repr(queue), "Queue: [1, 2] Front: 0 Back: 2")

    def test_empty_queue(self):
        queue = Queue()
        self.assertEqual(empty_queue(), queue)

    def test_enqueue(self):
        queue1 = Queue()
        queue2 = Queue()
        queue2.front = 0
        queue2.back = 1
        queue2.size = 1
        queue2.head = [1] + [None]*4999
        self.assertEqual(enqueue(queue1, 1), queue2)
        queue3 = Queue()
        queue3.size = 2
        queue3.front = 0
        queue3.back = 2
        queue3.head = [1, 2] + [None]*4998
        queue4 = Queue()
        queue4.front = 0
        queue4.back = 3
        queue4.size = 3
        queue4.head = [1, 2, 3] + [None]*4997
        self.assertEqual(enqueue(queue3, 3), queue4)

    def test_dequeue(self):
        queue1 = Queue()
        with self.assertRaises(IndexError):
            dequeue(queue1)
        queue2 = Queue()
        queue2.front = 0
        queue2.size = 3
        queue2.back = 3
        queue2.head = [1, 2, 3] + [None]*4997
        queue3 = Queue()
        queue3.size = 2
        queue3.front = 1
        queue3.back = 3
        queue3.head = [None] + [2, 3] + [None] * 4997
        self.assertEqual(dequeue(queue2), (1, queue3))

    def test_peek(self):
        queue1 = Queue()
        with self.assertRaises(IndexError):
            peek(queue1)
        queue2 = Queue()
        queue2.front = 0
        queue2.back = 3
        queue2.head = [1, 2, 3] + [None]*4997
        self.assertEqual(peek(queue2), 1)

    def test_size(self):
        queue1 = Queue()
        queue1.size = 3
        queue1.front = 0
        queue1.back = 3
        queue1.head = [1, 2, 3] + [None]*4997
        self.assertEqual(size(queue1), 3)

    def test_is_empty(self):
        queue1 = Queue()
        self.assertTrue(is_empty(queue1))
        queue2 = Queue()
        queue2.size = 3
        queue2.front = 0
        queue2.back = 3
        queue2.head = [1, 2, 3] + [None]*4997
        self.assertFalse(is_empty(queue2))

if __name__ == "__main__":
    unittest.main()

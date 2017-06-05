# Justin Mo

# Queue is a wrapper class
class Queue:
    def __init__(self):
        self.head = [None] * 5000
        self.capacity = 5000
        self.size = 0
        self.front = 0
        self.back = 0

    def __repr__(self):
        return "Queue: {!r} Front: {!r} Back: {!r}".format(self.head, self.front, self.back)

    def __eq__(self, other):
        return type(other) == Queue and self.head == other.head and self.size == other.size and self.front == other.front and self.back == other.back

# None -> Queue
# Takes no arguments and returns an empty queue.
def empty_queue():
    return Queue()

# Queue int -> Queue
# Takes in a Queue and a value and adds the value to the end of the Queue and returns the new Queue.
def enqueue(queue, val):
    queue.back += 1
    queue.head[queue.back - 1] = val
    queue.size += 1
    return queue

# Queue -> tuple(int, Queue)
# Takes in a Queue and removes the element at the beginning of the queue and returns a 2-tuple of the removed element and the new Queue.
def dequeue(queue):
    if queue.head == [None] * 5000:
        raise IndexError
    else:
        value = queue.head[queue.front]
        queue.head[queue.front] = None
        queue.front += 1
        queue.size -= 1
        return (value, queue)

# Queue -> int
# Takes in a Queue and returns the beginning of the Queue.
def peek(queue):
    if queue.head == [None] * 5000:
        raise IndexError
    else:
        return queue.head[queue.front]

# Queue -> int 
# Takes in a Queue and returns the size of the Queue.
def size(queue):
    return queue.size

# Queue -> bool
# Takes in a Queue and returns a bool depending on whether the Queue is empty.
def is_empty(queue):
    return queue == empty_queue()




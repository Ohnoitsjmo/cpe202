from linked_list import *
# Justin Mo

# Queue is a wrapper class
class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        return "Queue: {!r}".format(self.head)

    def __eq__(self, other):
        return type(other) == Queue and self.head == other.head and self.size == other.size

# None -> Queue
# Takes no arguments and returns an empty queue.
def empty_queue():
    return Queue()

# Queue int -> Queue
# Takes in a Queue and a value and adds the value to the end of the Queue and returns the new Queue.
def enqueue(queue, val):
    if queue.head == None:
        queue.size += 1
        queue.head = Pair(val, None)
        return queue
    else:
        queue.size += 1
        queue.head = add(queue.head, queue.size - 1, val)
        return queue

# Queue -> tuple(int, Queue)
# Takes in a Queue and removes the element at the beginning of the queue and returns a 2-tuple of the removed element and the new Queue.
def dequeue(queue):
	if queue.head == None:
		raise IndexError
	else:
		queue.head = reverse(queue)
		queue.size -= 1
		value = queue.head.first
		queue.head = queue.head.rest
		return (value, queue)

# Queue -> LinkedList
# Takes in a Queue and reverses it's head and returns the new linkedlist.
def reverse(queue):
	new_list = None
	counter = 0
	for i in range(0, queue.size):
		remove_tuple = remove(queue.head, counter)
		counter += 1
		value_removed = remove_tuple[0]
		new_list = add(new_list, 0, value_removed)
	return new_list
		
# Queue -> int
# Takes in a Queue and returns the beginning of the Queue.
def peek(queue):
	if queue.head == None:
		raise IndexError
	else:
		return queue.head.first

# Queue -> int
# Takes in a Queue and returns the size of the Queue.
def size(queue):
	return queue.size

# Queue -> bool
# Takes in a Queue and returns a bool depending on whether the Queue is empty.
def is_empty(queue):
	return queue == empty_queue()

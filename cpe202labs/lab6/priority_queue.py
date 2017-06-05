# Justin Mo

# PriorityQueue is a class that takes in a comes_before function and organizes a queue based on priority.
class PriorityQueue:
    def __init__(self, comes_before):
        self.comes_before = comes_before # a function
        self.head = [None] # Python built in array
        self.size = 0 # an int

    def __repr__(self):
        return "Queue: {!r}".format(self.head)

    def __eq__(self, other):
        return type(other) == PriorityQueue and self.head == other.head and self.size == other.size

# value value -> bool
# Takes in two nodes and compares their values and returns a bool based on the value.
def comes_before(a, b):
    return (a <= b)

# comes_before -> PriorityQueue
# Takes in an ordering function and returns an empty pqueue.
def empty_pqueue(comes_before):
    return PriorityQueue(comes_before)

# PriorityQueue value -> PriorityQueue
# Takes in a pqueue and a value and adds the value to the pqueue and returns the new pqueue.
def enqueue(pqueue, value):
    if pqueue.head == [None]:
        pqueue.head = [None, value]
        pqueue.size += 1
        return pqueue
    else:
        pqueue.size += 1
        pqueue.head.append(value)
        if pqueue.comes_before(pqueue.head[pqueue.size//2], value) == True:
            return pqueue
        else:
            parent_value = 2
            while pqueue.head[pqueue.size//parent_value] != None and pqueue.comes_before(pqueue.head[pqueue.size//parent_value], value) == False:
                old_parent = pqueue.head[pqueue.size//parent_value]
                pqueue.head[pqueue.size//parent_value] = value
                pqueue.head[pqueue.size//int(parent_value/2)] = old_parent
                parent_value *= 2
            return pqueue
'''if pqueue.head == [None]:
        pqueue.head = [value]
        pqueue.size += 1
        return pqueue
    else:  
        pqueue.size += 1
        index = 0
        for each_element in pqueue.head:
            if each_element != None:
                if comes_before(value, each_element) == True:
                    pqueue.head += [None]
                    for i in range(index, pqueue.size):
                         pqueue.head[pqueue.size - i] = pqueue.head[pqueue.size - i - 1]
                    pqueue.head[index] = value
                    return pqueue
                elif comes_before(value, each_element) == False and pqueue.size == index + 2:
                    pqueue.head.append(value)
                    return pqueue
                else:
                    index += 1
            else:
                return pqueue'''

# PriorityQueue -> tuple
# Takes in a pqueue and removes the element at the beginning of the pqueue and returns the element removed and the new pqueue in that order.
def dequeue(pqueue):
    if pqueue.head == [None]:
        raise IndexError
    elif pqueue.size == 1:
        value_removed = pqueue.head[1]
        pqueue.size -= 1
        pqueue.head = [None]
        return (value_removed, pqueue)
    else:
        value_removed = pqueue.head[1]
        pqueue.size -= 1
        root_node = pqueue.head[pqueue.size + 1]
        index1 = 2
        pqueue.head[1] = root_node
        while index1 <= pqueue.size and (pqueue.comes_before(root_node, pqueue.head[index1]) == False or pqueue.comes_before(root_node, pqueue.head[index1 + 1]) == False):
            if pqueue.comes_before(pqueue.head[index1], pqueue.head[index1 + 1]) == True:
                new_root = pqueue.head[index1]
                pqueue.head[index1//2] = new_root
                pqueue.head[index1] = root_node
                index1 *= 2
            else:
                new_root = pqueue.head[index1 + 1]
                pqueue.head[index1//2] = new_root
                pqueue.head[index1 + 1] = root_node
                index1 = 2*(index1 + 1)
        pqueue.head.pop(pqueue.size + 1)
        return (value_removed, pqueue)

'''for i in range(1, pqueue.size + 1):
            pqueue.head[i] = pqueue.head[i + 1]
        pqueue.head.pop(pqueue.size)
        return (value_removed, pqueue)'''

# PriorityQueue -> value
# Takes in a pqueue and returns the element at the beginning of the pqueue. 
def peek(pqueue):
    return pqueue.head[1]

# PriorityQueue -> int
# Takes in a pqueue and returns the size.
def size(pqueue):
    return pqueue.size

# PriorityQueue -> bool
# Takes in a pqueue and returns a bool depending on whether it's empty.
def is_empty(pqueue):
    return (pqueue == empty_pqueue(comes_before))


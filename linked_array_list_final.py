# Justin Mo
# Linked List
# AnyList is one of
# -- Pair(first, rest)
# -- None
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest

def add(lst, index, val, counter=0):
    if index == 0:
        return Pair(val, lst)
    elif lst is None and counter == 0:
        return Pair(val, None)
    elif index == counter:
        return Pair(val, lst)
    return Pair(lst.first, add(lst.rest, index, val, counter+1))

def get(lst, index, counter=0):
    if counter == 0 and lst is None:
        raise IndexError
    elif index == counter:
        return lst.first
    return get(lst.rest, index, counter+1)

def remove_helper(lst, index, counter=0):
    if counter == index:
        return lst.rest
    return Pair(lst.first, remove_helper(lst.rest, index, counter+1))

def remove(lst, index):
    if lst is None:
        raise IndexError
    return (get(lst, index), remove_helper(lst, index))

lst = Pair(1, Pair(2, Pair(3, None)))

def contains(lst, value):
    if lst is None:
        return False
    elif lst.first == value:
        return True
    return contains(lst.rest, value)

# class AnyList is one of
# -- ArrayList
class ArrayList:
    def __init__(self):
        self.array = [None] * 8
        self.capacity = 8
        self.size = 0

    def __repr__(self):
        return "Capacity: {!r}, Size: {!r}, Array: {!r}".format(self.capacity, self.size, self.array)

    def __eq__(self, other):
        return type(other) == ArrayList and self.array == other.array and self.capacity == other.capacity and self.size == other.size

def add(lst, index, val):
    if lst.array == None:
        lst.size += 1
        lst.array = [val] + [None] * 7
        return lst
    else:
        if lst.capacity == lst.size:
            lst.capacity = lst.capacity * 2
            lst.array += [None] * lst.capacity
        if index == lst.size - 1:
            lst.array += [None]
        for i in range(0, lst.size - index):
            lst.array[lst.size - i] = lst.array[lst.size - i - 1]
        lst.array[index] = val
        lst.size += 1
        return lst

def remove(lst, index):
    if lst is None:
        raise IndexError
    else:
        for i in range(index, lst.size - 1):
            lst.array[i] = lst.array[i + 1]
        lst.array.pop()
        lst.size -= 1
        return lst

def get(lst, index)
    return lst.array[index]

def contains(lst, val):
    for each_val in lst.array:
        if each_val = val:
            return True
    return False



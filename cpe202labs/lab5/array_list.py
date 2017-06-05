# Justin Mo

# ArrayList is a
# -- List
class List:
    def __init__(self):
        self.array = [None]*10 # an array list
        self.length = 0 # an int
        self.capacity = 10 # an int

    def __repr__(self):
        c = "{:s}".format(str(self.array[0]))
        for i in self.array[1:self.length]:
            c += ", {:s}".format(str(i))
        return c

    def __eq__(self, other):
        if type(other) != List:
            return False
        else: 
            bool = True 
            for i in range(self.length - 1):
                if self.array[i] != other.array[i]:
                    bool = False
            return type(other) == List and bool and self.length == other.length and self.capacity == other.capacity

# None -> None
# takes in no arguments and returns an empty list
def empty_list():
    return List()

# ArrayList -> int
# takes in an array and returns the length of the list
def length(arraylist):
    if arraylist == None:
        return 0
    return arraylist.length

# ArrrayList int value -> ArrayList
# takes in an array, an index, and a value and returns a new array with the value inserted at the given index
def add(arraylist, index, value):
    if arraylist == List() and index == 0:
	    arraylist.array[index] = value
	    arraylist.length += 1
	    return arraylist
    if arraylist.length == index:
	    arraylist.length += 1
	    arraylist.array += [None]
	    arraylist.array[index] = value
	    return arraylist
    if arraylist == List() or index < 0 or arraylist.length < index:
	    raise IndexError
    else:
        if arraylist.length == arraylist.capacity:
            arraylist.capacity += 10
            new_array = [None] * (arraylist.capacity + 10)
            for i in range(arraylist.length):
                new_array[i] = arraylist.array[i]
            arraylist.array = new_array
        for i in range(index, arraylist.length):
            arraylist.array[arraylist.length - i] = arraylist.array[arraylist.length - i - 1]
        arraylist.array[index] = value
        arraylist.length += 1
        return arraylist

# ArrayList int -> int
# takes in array and an index and returns the value at that index
def get(arraylist, index):
    if arraylist.length <= index  or arraylist == List() or index < 0:
        raise IndexError
    return arraylist.array[index]

# ArrayList int value -> ArrayList
# takes in arraylist, an index, and a value and returns a new list where the value at the given index is replaced by the new given value
def set(arraylist, index, value):
    if arraylist.length <= index or arraylist == List() or index < 0:
        raise IndexError
    arraylist.array[index] = value
    return arraylist

# ArrayList int -> tuple
# takes in arraylist and an index and returns a tuple containinng the value removed and the resulting list
def remove(arraylist, index):
    if arraylist == List() or index < 0 or arraylist.length <= index:
        raise IndexError
    else:
        value = arraylist.array[index]
        arraylist.length -= 1
        for i in range(index, arraylist.length):
            arraylist.array[i] = arraylist.array[i + 1]
        return (value, arraylist)

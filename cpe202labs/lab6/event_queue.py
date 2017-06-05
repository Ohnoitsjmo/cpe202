# Justin Mo 
from priority_queue import *
import time

# class EventQueue is a wrapper class that uses priority queue and tracks a virtual time.
class EventQueue:
    def __init__(self):
        self.time = 0 # an int
        self.pqueue = PriorityQueue(event_delay) # a PriorityQueue

    def __eq__(self):
        type(other) == EventQueue and self.time == other.time and self.pqueue == other.pqueue

# Event is a class that takes in a function and organizes a queue based on priority.
class Event:
    def __init__(self, func, delay):
        self.func = func # a function
        self.delay = delay # an int

    def __eq__(self, other):
        return type(other) == Event and self.func == other.func and self.delay == other.delay

# EventQueue function int -> None
# Takes in an equeue and function and time delay and stores it in the equeue.
def add_event(equeue, func, delay):
    equeue.pqueue = enqueue(equeue.pqueue, Event(func, delay))

# EventQueue -> None
# Takes in an equeue and for as long as there are events, the function will wait until the next event is ready to execute. The function will then execute all ready events.
def run_events(equeue):
    while equeue.pqueue.size != 0:
        tple = dequeue(equeue.pqueue)
        equeue.pqueue = tple[1]
        equeue.time += tple[0].delay
        tple[0].func(equeue)
        time.sleep(tple[0].delay)

# Event Event -> bool
# Takes in two events and returns a bool based on whether the first event has a smaller delay than the second.
def event_delay(e1, e2):
    return (e1.delay <= e2.delay)

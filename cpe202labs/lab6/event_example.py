# Justin Mo
from event_queue import *
import sys
 
def print_each_second(equeue):
   print('\ttime {}: every one'.format(equeue.time))
   add_event(equeue, print_each_second, 1)
 
def print_each_five(equeue):
   print('\ttime {}: every five'.format(equeue.time))
   add_event(equeue, print_each_second, 1)

def stop(equeue):
   print('\ttime {}: stopping'.format(equeue.time))
   sys.exit(0)

if __name__ == '__main__':
   equeue = EventQueue()

   add_event(equeue, stop, 15)   
   add_event(equeue, stop, 20)
   add_event(equeue, print_each_five, 5)
   add_event(equeue, print_each_second, 1)

   run_events(equeue)

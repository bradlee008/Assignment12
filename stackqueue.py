#
#  stack.py, a simple stack class
#
#
class Stack:
    """ Provides a rudimentary stack class """

    def __init__(self, initial_contents = []):
        self.stack = initial_contents[:]

    def is_empty(self):
        return self.stack == []

    def add(self, item):
        self.stack.append(item)

    def remove(self):
        return self.stack.pop()

    def __str__(self):
        return "The stack contains: " + str(self.stack)
    

class Queue:
    """ Provides a rudimentary queue class. """

    def __init__(self, initial_contents=[]):
        self.queue = initial_contents[:]

    def is_empty(self):
        return self.queue == []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        return self.queue.pop(0)

    def __str__(self):
        return "The queue contains: " + str(self.queue)

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
import sys
sys.path.append("../singly_linked_list")
import singly_linked_list

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = singly_linked_list.LinkedList()

    def __len__(self):
        return self.storage.length()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if self.__len__() > 0:
            return self.storage.remove_head()

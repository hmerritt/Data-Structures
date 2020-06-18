class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        # Is list empty
        return self.head is None and self.tail is None

    def get_max(self):
        if self.isEmpty():
            return None

        max = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max:
                max = current_node.value
            current_node = current_node.next_node
        return max

    def add_to_head(self, value):
        node = Node(value)

        # Is list empty
        if self.isEmpty():
            self.head = node
            self.tail = node

        else:
            # Point to head
            node.next_node = self.head

            # Move head to new node
            self.head = node

    def add_to_tail(self, value):
        node = Node(value)

        # Is list empty
        if self.isEmpty():
            self.head = node
            self.tail = node

        else:
            # Point to tail
            self.tail.next_node = node
            self.tail = node

    def remove_head(self):
        if not self.head:
            return None

        head = self.head.value

        if self.head.next_node is None:
            self.head = None
            self.tail = None
            return head

        self.head = self.head.next_node
        return head

    def contains(self, value):
        if self.isEmpty():
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node

        return False

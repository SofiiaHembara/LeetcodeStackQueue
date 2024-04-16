class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head:
            item_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return item_value
        raise ValueError('Queue is empty.')

    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if not self.is_empty():
            return self.head.value
        raise ValueError('Queue is empty.')

class MyStack:
    def __init__(self) -> None:
        self.queue = Queue()

    def push(self, value):
        self.queue.add(value)
        for _ in range(1, self.queue_length()):
            self.queue.add(self.queue.pop())

    def pop(self):
        if not self.empty():
            return self.queue.pop()
        raise ValueError('Stack is empty.')

    def top(self):
        if not self.empty():
            return self.queue.peek()
        raise ValueError('Stack is empty.')

    def empty(self):
        return self.queue.is_empty()

    def queue_length(self):
        current = self.queue.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
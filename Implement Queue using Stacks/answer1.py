class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self):
        return self.head is None


class MyQueue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x:int) -> None:
        self.stack1.push(x)
    
    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    
    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
from collections import defaultdict

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def remove(self, node_to_remove):
        if not self.head:
            return
        if self.head == node_to_remove:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next != node_to_remove:
            current = current.next
        if current.next:
            current.next = current.next.next

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0
        self.all_elements = LinkedList()

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.freq[x] > self.max_freq:
            self.max_freq = self.freq[x]
        self.group[self.freq[x]].append(x)
        self.all_elements.append(x)

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x
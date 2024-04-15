class MyStack:
    def __init__(self) -> None:
        self.queue = []

    def push(self, value):
        self.queue.append(value)
    
    def pop(self):
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
    def top(self):
        if self.queue:
            return self.queue[-1]
        return None
    
    def empty(self):
        return len(self.queue) == 0

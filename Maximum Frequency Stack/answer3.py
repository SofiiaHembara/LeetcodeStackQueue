class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stack = {}

    def push(self, val: int) -> None:
        value_count = 1 + self.count.get(val, 0)
        self.count[val] = value_count
        if value_count > self.max_count:
            self.max_count = value_count
            self.stack[value_count] = []
        self.stack[value_count].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_count].pop()
        self.count[res] -= 1
        if not self.stack[self.max_count]:
            self.max_count -= 1
        return res 
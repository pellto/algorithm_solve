class CustomStack:
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize


    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        return -1 if len(self.stack) == 0 else self.stack.pop(-1)

    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

    def __repr__(self):
        return f"{self.stack}"


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

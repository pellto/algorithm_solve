import sys
from collections import deque


class MyStack:
    def __init__(self):
        self.queue: deque[int] = deque()
        self.poper: deque[int] = deque()

    def push(self, x: int) -> None:
        if len(self.poper) != 0:
            self.queue.append(self.poper.popleft())
        self.poper.append(x)

    def pop(self) -> int:
        out = self.poper.popleft()
        temp = deque()
        while len(self.queue) > 1:
            temp.append(self.queue.popleft())
        self.poper, self.queue = self.queue, temp
        return out

    def top(self) -> int:
        return self.poper[0]

    def empty(self) -> bool:
        return len(self.poper) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == "__main__":
    commands = ["MyStack", "push", "push", "top", "pop", "empty"]
    nums = [[], [1], [2], [], [], []]
    outputs = [None, None, None, 2, 2, False]
    results = []
    stack: MyStack
    for command, num in zip(commands, nums):
        if command == "MyStack":
            stack = MyStack()
            results.append(None)
        elif command == "push":
            stack.push(num[0])
            results.append(None)
        elif command == "top":
            results.append(stack.top())
        elif command == "pop":
            results.append(stack.pop())
        else:
            results.append(stack.empty())

    for expect, result in zip(outputs, results):
        if expect != result:
            print("FAIL")
            sys.exit()
    print("SUCCESS")

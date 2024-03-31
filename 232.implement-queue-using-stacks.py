import sys
from typing import List


class MyQueue:
    def __init__(self):
        self._input: List[int] = []
        self._out: List[int] = []

    def push(self, x: int) -> None:
        self._input.append(x)

    def pop(self) -> int:
        if len(self._out) > 0:
            return self._out.pop()
        while len(self._input) > 1:
            self._out.append(self._input.pop())
        return self._input.pop()

    def peek(self) -> int:
        if len(self._out) > 0:
            return self._out[-1]

        while len(self._input) > 0:
            self._out.append(self._input.pop())
        return self._out[-1]

    def empty(self) -> bool:
        return len(self._input) == len(self._out) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
    commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    nums = [[], [1], [2], [], [], []]
    outputs = [None, None, None, 1, 1, False]
    results = []
    q: MyQueue
    for command, num in zip(commands, nums):
        if command == "MyQueue":
            q = MyQueue()
            results.append(None)
        elif command == "push":
            q.push(num[0])
            results.append(None)
        elif command == "peek":
            results.append(q.peek())
        elif command == "pop":
            results.append(q.pop())
        else:
            results.append(q.empty())
    print(results)
    for expect, result in zip(outputs, results):
        if expect != result:
            print("FAIL")
            sys.exit()
    print("SUCCESS")

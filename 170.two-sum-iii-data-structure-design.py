import sys
from typing import List


class TwoSum:
    arr: List[int] = []
    sums: set = set()

    def __init__(self):
        return

    def add(self, number: int) -> None:
        if len(self.arr) == 0:
            self.sums.add(number)
        for num in self.arr:
            self.sums.add(num + number)
        self.arr.append(number)

    def find(self, value: int) -> bool:
        return value in self.sums


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


if __name__ == "__main__":
    s = TwoSum()
    inputs = ["TwoSum", "add", "add", "find"]
    nums = [[], [1], [2], [1]]
    outputs = [None, None, None, True]
    real = []
    for idx, _input in enumerate(inputs):
        if _input == "TwoSum":
            real.append(None)
        elif _input == "add":
            s.add(nums[idx][0])
            real.append(None)
        else:
            real.append(s.find(nums[idx][0]))

    print(s.sums)
    print(real)
    for r, o in zip(real, outputs):
        if r != o:
            print("FAIL")
            sys.exit()
    print("SUCCESS")

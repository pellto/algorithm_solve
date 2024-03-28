from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)
        return list(map(int, list(str(int(s) + 1))))


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(s.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(s.plusOne([9]))  # [1, 0]

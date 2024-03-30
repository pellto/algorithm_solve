from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checker = set()
        for num in nums:
            if num in checker:
                checker.remove(num)
            else:
                checker.add(num)
        return checker.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))  # 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
    print(s.singleNumber([1]))  # 1

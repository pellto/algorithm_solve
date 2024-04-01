from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([3, 2, 1]))  # 1
    print(s.thirdMax([2, 1]))  # 2
    print(s.thirdMax([2, 2, 3, 1]))  # 1

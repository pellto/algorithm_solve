from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = (n * (n + 1)) // 2
        return _sum - sum(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))  # 2
    print(s.missingNumber([0, 1]))  # 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
    print(s.missingNumber([1]))  # 0
    print(s.missingNumber([0]))  # 1

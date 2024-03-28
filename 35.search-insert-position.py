from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # 4
    print(s.searchInsert([1, 3, 4, 10, 11], 5))  # 3
    print(s.searchInsert([1, 3, 5, 6], 0))  # 0
    print(s.searchInsert([1], 1))  # 0
    print(s.searchInsert([1, 3], 0))  # 0
    print(s.searchInsert([1, 3], 10))  # 2
    print(s.searchInsert([1, 3, 4, 5, 10], 0))  # 0

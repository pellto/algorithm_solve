from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set([i for i in range(1, len(nums) + 1)])
        nums_set = set(nums)
        return list(all_nums - nums_set)


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
    print(s.findDisappearedNumbers([1, 1]))  # [2]

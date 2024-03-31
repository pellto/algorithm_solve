from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moving_nums = []
        zero_cnt = 0
        for idx, num in enumerate(nums):
            if num != 0:
                moving_nums.append(num)
            else:
                zero_cnt += 1
        if len(nums) == zero_cnt:
            return
        length = len(moving_nums)
        for idx, num in enumerate(moving_nums):
            nums[idx] = num

        for idx in range(zero_cnt):
            nums[length + idx] = 0


if __name__ == "__main__":
    s = Solution()
    p1 = [0, 1, 0, 3, 12]
    p2 = [0]
    s.moveZeroes(p1)
    print(p1)  # [1,3,12,0,0]
    s.moveZeroes(p2)
    print(p2)  # [0]

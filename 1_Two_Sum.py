class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__=="__main__":
    Solution().twoSum([2,7,11,15], 9)

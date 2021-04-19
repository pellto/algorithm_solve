class Solution:
    """
    Runtime: 56 ms, faster than 59.20%
    Memory Usage: 14.9 MB, less than 94.47%
    """
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums = sorted(nums)

        ans = 0
        for i in range(0, len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        return ans


if __name__=="__main__":
    print(Solution().maximumGap([3,6,9,1]))
    print(Solution().maximumGap([10]))

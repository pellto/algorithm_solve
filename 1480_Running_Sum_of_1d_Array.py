class Solution:
    def runningSum(self, nums):
        ret = [nums[0]]
        for i in range(1, len(nums)):
            ret.append(ret[i-1]+nums[i])
        return ret


if __name__=="__main__":
    print(Solution().runningSum([1,2,3,4]))
    print(Solution().runningSum([1,1,1,1,1]))
    print(Solution().runningSum([3,1,2,10,1]))

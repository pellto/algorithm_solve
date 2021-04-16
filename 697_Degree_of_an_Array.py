class Solution:
    def findShortestSubArray(self, nums):
        start_index, end_index, counter = {}, {}, {}
        for i in range(len(nums)):
            if nums[i] not in start_index:
                start_index[nums[i]] = i
            if nums[i] not in counter:
                counter[nums[i]] = 0
            counter[nums[i]] += 1
            end_index[nums[i]] = i

        ret = len(nums)
        _max = max(counter.values())
        for key in counter:
            if counter[key] == _max:
                ret = min(end_index[key] - start_index[key] + 1, ret)

        return ret


if __name__=="__main__":
    print(Solution().findShortestSubArray([1,2,2,3,1]))  #2
    print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))  #6
    print(Solution().findShortestSubArray([1,2,1,3,3,3,2,1]))  #3

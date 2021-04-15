class Solution:
    def fourSum(self, nums, target):
        out = set()
        length = len(nums)
        nums = sorted(nums)

        for i in range(length-3):
            for j in range(i+1, length-2):
                new_target = target - nums[i] - nums[j]

                k, l = j + 1, length - 1
                while k < l:
                    if nums[k] + nums[l] == new_target:
                        out.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] < new_target:
                        k += 1
                    else:
                        l -= 1
        return list(map(list, out))


if __name__=="__main__":
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))
    print(Solution().fourSum([2,2,2,2,2], 8))
    

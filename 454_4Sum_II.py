class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        cnt = 0
        temp = {}
        for n1 in nums1:
            for n2 in nums2:
                key = n1 + n2
                if key not in temp:
                    temp[key] = 0
                temp[key] += 1

        for n3 in nums3:
            for n4 in nums4:
                key = -(n3 + n4)
                if key in temp:
                    cnt += temp[key]
        return cnt


if __name__=="__main__":
    print(Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
    print(Solution().fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]))
    

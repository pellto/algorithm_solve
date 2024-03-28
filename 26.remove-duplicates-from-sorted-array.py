from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        dup = set()
        for num in nums:
            if num not in dup:
                cnt += 1
            dup.add(num)
        dup_li = sorted(list(dup))

        for i in range(len(nums)):
            if i < cnt:
                nums[i] = dup_li[i]
            else:
                nums[i] = -0
        return cnt


if __name__ == "__main__":
    s = Solution()
    p1 = [1, 1, 2]
    print(s.removeDuplicates(p1))  # 2, nums = [1,2,_]
    print("p1 >> ", p1)
    p2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(p2))  # 5, nums = [0,1,2,3,4,_,_,_,_,_]
    print("p2 >> ", p2)
    p3 = [-1, 0, 0, 0, 0, 3, 3]
    print(s.removeDuplicates(p3))  # 3, nums = [-1,0,3]
    print("p3 >> ", p3)

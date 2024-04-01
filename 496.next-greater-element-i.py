from typing import List


class Solution:
    def nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        nextGreaterElementMap = dict()
        stack = []
        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                nextGreaterElementMap[stack.pop()] = num
            stack.append(num)

        while len(stack) > 0:
            nextGreaterElementMap[stack.pop()] = -1

        out = []
        for num in nums1:
            out.append(nextGreaterElementMap[num])
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1, 3, -1]
    print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3, -1]
    print(
        s.nextGreaterElement(
            [11, 37, 32, 47, 35, 33, 44, 22], [11, 37, 32, 47, 35, 33, 44, 22]
        )
    )  # [47, 44, 33, -1, 44, 44, -1, -1]
    print(
        s.nextGreaterElement([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
    )  # [2,3,4,5,6,7,-1]
    print(
        s.nextGreaterElement([7, 6, 5, 4, 3, 2, 1], [7, 6, 5, 4, 3, 2, 1])
    )  # [-1, -1, -1, -1, -1, -1, -1]

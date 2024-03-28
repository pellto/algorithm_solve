from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m] + nums2
        for i, n in enumerate(sorted(tmp)):
            nums1[i] = n


if __name__ == "__main__":
    s = Solution()
    p1 = [1, 2, 3, 0, 0, 0]
    p2 = [1]
    p3 = [0]
    s.merge(p1, 3, [2, 5, 6], 3)
    s.merge(p2, 1, [], 0)
    s.merge(p3, 0, [1], 1)
    print("p1 >> ", p1)  # [1,2,2,3,5,6]
    print("p2 >> ", p2)  # [1]
    print("p3 >> ", p3)  # [1]

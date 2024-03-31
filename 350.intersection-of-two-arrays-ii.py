from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = dict(), dict()
        set1, set2 = set(), set()
        for num in nums1:
            counter1[num] = counter1.get(num, 0) + 1
            set1.add(num)
        for num in nums2:
            counter2[num] = counter2.get(num, 0) + 1
            set2.add(num)
        out = []
        for num in list(set1.intersection(set2)):
            for _ in range(min(counter1[num], counter2[num])):
                out.append(num)
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]

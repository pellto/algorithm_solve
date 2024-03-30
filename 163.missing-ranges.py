from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        if lower == upper and nums[0] == lower:
            return []
        arr = []
        if lower < nums[0]:
            arr.append(lower - 1)
        arr = arr + nums
        if nums[-1] < upper:
            arr.append(upper + 1)

        out = []
        for i in range(len(arr) - 1):
            start, end = arr[i] + 1, arr[i + 1] - 1
            if end - start >= 0:
                out.append([start, end])
        return out


if __name__ == "__main__":
    s = Solution()
    print(
        s.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
    )  # [[2,2],[4,49],[51,74],[76,99]]
    print(s.findMissingRanges([-1], -1, -1))  # []
    print(s.findMissingRanges([], 1, 1))  # []

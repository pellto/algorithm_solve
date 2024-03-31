from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        idx = 0
        while idx < len(nums):
            summary = f"{nums[idx]}"
            j = idx + 1
            checker = False
            while j < len(nums) and nums[idx] + 1 == nums[j]:
                checker = True
                idx, j = j, j + 1
            if checker:
                summary += f"->{nums[idx]}"
            out.append(summary)
            idx += 1
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]

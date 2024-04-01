from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sequence_num = -1
        consecutive_ones = 0
        for n in nums:
            if n == 0:
                sequence_num = max(sequence_num, consecutive_ones)
                consecutive_ones = 0
            else:
                consecutive_ones += 1
        sequence_num = max(sequence_num, consecutive_ones)
        return sequence_num


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
    print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 2

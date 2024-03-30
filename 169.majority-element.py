from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        max_cnt = -1
        out = -1
        for num in counter:
            if counter[num] > max_cnt:
                max_cnt = counter[num]
                out = num
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))  # 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2

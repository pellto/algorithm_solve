from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        saver = dict()
        for i, num in enumerate(nums):
            if num in saver:
                if abs(saver[num] - i) <= k:
                    return True
            saver[num] = i
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
    print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False

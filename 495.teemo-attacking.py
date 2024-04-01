from typing import List


class Solution:
    def findPoisonedDuration(
        self, timeSeries: List[int], duration: int
    ) -> int:
        last_attacked_at = max(timeSeries)
        timeSeries_set = set(timeSeries)
        poisoned_time = 0
        temp_duration = 0
        for attack_time in range(last_attacked_at + duration):
            if attack_time in timeSeries_set:
                temp_duration = duration
            if temp_duration != 0:
                poisoned_time += 1
                temp_duration -= 1
        return poisoned_time


if __name__ == "__main__":
    s = Solution()
    print(s.findPoisonedDuration([1, 4], 2))  # 4
    print(s.findPoisonedDuration([1, 2], 2))  # 3

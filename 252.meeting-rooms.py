from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        attends = [intervals[0]]
        for interval in intervals[1:]:
            for attend in attends:
                print("interval >> ", interval, "attend >> ", attend)
                if (
                    attend[0] <= interval[0] < attend[1]
                    or attend[0] < interval[1] <= attend[1]
                    or interval[0] <= attend[0] < interval[1]
                    or interval[0] < attend[1] <= interval[1]
                ):
                    return False
            attends.append(interval)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # False
    print(s.canAttendMeetings([[7, 10], [2, 4]]))  # True
    print(s.canAttendMeetings([]))  # True
    print(s.canAttendMeetings([[0, 30], [60, 240], [90, 120]]))  # False
    print(s.canAttendMeetings([[8, 11], [17, 20], [17, 20]]))  # False
    print(s.canAttendMeetings([[13, 15], [1, 13]]))  # True

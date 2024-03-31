from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        out = []
        hours = [bin(n) for n in range(12)]
        minutes = [bin(n) for n in range(60)]
        for hour in hours:
            for minute in minutes:
                if hour.count("1") + minute.count("1") == turnedOn:
                    h, m = int(hour, 2), f"{int(minute, 2)}".zfill(2)
                    out.append(f"{h}:{m}")

        return out


if __name__ == "__main__":
    s = Solution()
    print(
        s.readBinaryWatch(1)
    )  # ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    print(s.readBinaryWatch(9))  # []

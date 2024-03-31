from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n + 1):
            out.append(bin(i)[2:].count("1"))
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))  # [0,1,1]
    print(s.countBits(5))  # [0,1,1,2,1,2]

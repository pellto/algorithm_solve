class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        n = 2
        while n * n <= x:
            n += 1
        return n - 1


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))  # 2
    print(s.mySqrt(8))  # 2

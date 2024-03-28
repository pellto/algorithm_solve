class Solution:
    def climbStairs(self, n: int) -> int:
        a0, a1 = 1, 1
        if n == 0:
            return 0
        for _ in range(n):
            a2 = a0 + a1
            a0, a1 = a1, a2
        return a0


# 1 = 1 = 1
# 2 = 11, 2 = 2
# 3 = 111, 12, 21 = 3
# 4 = 1111, 112, 121, 211, 22 = 5
# 5 = 11111, 1112, 1121, 1211, 2111, 122, 212, 221 = 8
# 6 = 111111, 11112, 11121, 11211, 12111, 21111, 1122, 1212, 1221, 2112, 2121, 2211, 222 = 13

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(0))  # 0
    print(s.climbStairs(1))  # 1
    print(s.climbStairs(2))  # 2 = 1 + 1, 2
    print(s.climbStairs(3))  # 3 = 1 + 1, 1 + 2, 2 + 1
    print(s.climbStairs(6))  # 13

class Solution:
    def uniquePaths(self, m, n):
        """
        Runtime: 28 ms, faster than 84.66%
        Memory Usage: 14.4 MB, less than 38.84%
        """
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        for y in range(m):
            for x in range(n):
                if y == 0 or x == 0:
                    dp[y][x] = 1
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]


if __name__=="__main__":
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))
    print(Solution().uniquePaths(2, 3))

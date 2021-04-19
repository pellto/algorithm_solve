class Solution:
    """
    Runtime : 88ms, faster than 5.20%
    Memory  : 14.3MB, less than 83.53%
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp = []
        for i in range(len(obstacleGrid)):
            dp.append([0] * len(obstacleGrid[0]))

        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if y == 0 and x == 0:
                    dp[y][x] = 1
                    continue
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    if x == 0:
                        dp[y][x] = dp[y-1][x]
                    elif y == 0:
                        dp[y][x] = dp[y][x-1]
                    else:
                        dp[y][x] = dp[y-1][x] + dp[y][x-1]

                print(dp)
        return dp[-1][-1]


if __name__=="__main__":
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # 2
    print(Solution().uniquePathsWithObstacles([[0,1], [0,0]])) # 1
    print(Solution().uniquePathsWithObstacles([[1]])) # 0
    print(Solution().uniquePathsWithObstacles([[0, 0], [0, 1]])) # 0

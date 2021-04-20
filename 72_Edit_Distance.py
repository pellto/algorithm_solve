class Solution:
    def minDistance(self, word1, word2):
        """
        Runtime: 160 ms, faster than 76.25%
        Memory Usage: 17.7 MB, less than 64.04%
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

        for i in range(l2 + 1):
            dp[i][0] = i
        for j in range(l1 + 1):
            dp[0][j] = j

        for i in range(l2):
            for j in range(l1):
                if word1[j] != word2[i]:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                else:
                    dp[i+1][j+1] = dp[i][j]

        return dp[l2][l1]


if __name__=="__main__":
    print(Solution().minDistance("horse", "ros")) # 3
    print(Solution().minDistance("intention", "execution")) # 5
    print(Solution().minDistance("aaa", "aaaaa")) # 2

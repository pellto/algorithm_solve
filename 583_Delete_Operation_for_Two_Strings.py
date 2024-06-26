class Solution:
    def minDistance(self, word1, word2):
        """
        Runtime: 312 ms, faster than 47.17%
        Memory Usage: 17.9 MB, less than 25.00%
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[l1][l2]


if __name__=="__main__":
    print(Solution().minDistance("sea", "eat")) # 2
    print(Solution().minDistance("leetcode", "etco")) # 4

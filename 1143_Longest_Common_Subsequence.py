class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """
        Runtime: 448 ms, faster than 44.66%
        Memory Usage: 21.9 MB, less than 80.16%
        """
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(l2 + 1):
            for j in range(l1 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l2][l1]


if __name__=="__main__":
    print(Solution().longestCommonSubsequence("abcde", 'ace')) # 3
    print(Solution().longestCommonSubsequence("abc", 'abc')) # 3
    print(Solution().longestCommonSubsequence("abc", 'def')) # 0

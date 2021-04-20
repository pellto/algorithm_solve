class Solution:
    def longestPalindromeSubseq(self, s):
        """
        Runtime: 3096 ms, faster than 18.94%
        Memory Usage: 39.6 MB, less than 32.01%
        """
        length = len(s)
        r_s = s[::-1]
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                if s[i - 1] == r_s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[length][length]


if __name__=="__main__":
    print(Solution().longestPalindromeSubseq("bbbab")) # 4
    print(Solution().longestPalindromeSubseq("cbbd")) # 2

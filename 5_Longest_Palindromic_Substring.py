class Solution:
    def longestPalindrome(self, s):
        """
        Runtime: 84 ms, faster than 99.23%
        Memory Usage: 14 MB, less than 99.18%
        """
        i, l = 0, 0
        for j in range(len(s)):
            if s[j-l:j+1] == s[j-l:j+1][::-1]:
                i, l = j-l, l+1

            elif j > l and s[j-l-1:j+1] == s[j-l-1:j+1][::-1]:
                i, l = j-l-1, l+2

        return s[i:i+l]


if __name__=="__main__":
    print(Solution().longestPalindrome("abcdaaefgh")) # aa
    print(Solution().longestPalindrome("babad")) # bab
    print(Solution().longestPalindrome("aba")) # aba
    print(Solution().longestPalindrome("cbbd")) # bb
    print(Solution().longestPalindrome("a")) # a
    print(Solution().longestPalindrome("ac")) # a
    print(Solution().longestPalindrome("aaaaa")) # aaaaa

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = dict()
        out = 0
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        odd_count = 0
        for c in counter:
            it = counter[c]
            while it // 2 >= 1:
                it -= 2
                out += 2
            if it == 1:
                odd_count += 1
        if odd_count:
            return out + 1
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))  # 7
    print(s.longestPalindrome("a"))  # 1
    print(s.longestPalindrome("ab"))  # 1
    print(s.longestPalindrome("abc"))  # 1
    print(s.longestPalindrome("abcd"))  # 1

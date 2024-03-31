class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = dict()
        for c in s:
            if c in counter and counter[c] == 1:
                counter[c] -= 1
            else:
                counter[c] = 1
        remain = sum(counter.values())
        return remain == 1 or remain == 0


if __name__ == "__main__":
    s = Solution()
    print(s.canPermutePalindrome("code"))  # False
    print(s.canPermutePalindrome("aab"))  # True
    print(s.canPermutePalindrome("carerac"))  # True
    print(s.canPermutePalindrome("aaa"))  # True

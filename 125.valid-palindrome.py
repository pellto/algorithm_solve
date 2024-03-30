class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain_string = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                plain_string += c.lower()
        return plain_string == plain_string[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))  # False
    print(s.isPalindrome(" "))  # True
    print(s.isPalindrome("0P"))  # False

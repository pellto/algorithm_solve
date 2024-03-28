class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome(121))  # True
    print(Solution().isPalindrome(-121))  # False
    print(Solution().isPalindrome(10))  # False

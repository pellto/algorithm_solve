class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n // 3 > 0:
            if n % 3 != 0:
                return False
            n //= 3
        return n == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(27))  # True
    print(s.isPowerOfThree(9))  # True
    print(s.isPowerOfThree(3))  # True
    print(s.isPowerOfThree(0))  # False
    print(s.isPowerOfThree(-1))  # False

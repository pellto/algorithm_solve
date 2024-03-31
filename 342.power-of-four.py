class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(16))  # True
    print(s.isPowerOfFour(5))  # False
    print(s.isPowerOfFour(1))  # True

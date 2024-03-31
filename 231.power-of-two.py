class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # while n > 1 and n % 2 == 0:
        #     n //= 2
        # return n == 0 or n == 1
        if n < 0:
            return False
        return bin(n).count("1") == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(1))  # True
    print(s.isPowerOfTwo(16))  # True
    print(s.isPowerOfTwo(3))  # False
    print(s.isPowerOfTwo(233))  # False
    print(s.isPowerOfTwo(-16))  # False

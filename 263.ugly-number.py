class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugly_numbers = [2, 3, 5]
        while n > 1:
            checker = True
            for ugly in ugly_numbers:
                if n % ugly == 0:
                    checker = False
                    n //= ugly
            if checker:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6))  # True
    print(s.isUgly(1))  # True
    print(s.isUgly(14))  # False

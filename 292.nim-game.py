class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == "__main__":
    s = Solution()
    print(s.canWinNim(4))  # False
    print(s.canWinNim(1))  # True
    print(s.canWinNim(2))  # True

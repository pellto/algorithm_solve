class Solution:
    def arrangeCoins(self, n: int) -> int:
        _sum = 0
        for i in range(1, n + 1):
            _sum += i
            if _sum == n:
                return i
            elif _sum > n:
                return i - 1
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.arrangeCoins(5))  # 2
    print(s.arrangeCoins(8))  # 3

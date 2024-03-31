class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            num = sum(map(int, list(str(num))))
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(38))  # 2
    print(s.addDigits(0))  # 0

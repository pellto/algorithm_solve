class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        out = ""
        n = abs(num)
        while n // 7 != 0:
            out += str(n % 7)
            n //= 7
        if n != 0:
            out += str(n)
        if num < 0:
            out += "-"
        return out[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.convertToBase7(100))  # "202"
    print(s.convertToBase7(-7))  # "-10"
    print(s.convertToBase7(0))  # "0"

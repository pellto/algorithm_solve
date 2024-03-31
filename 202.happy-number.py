class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            str_n = str(n)
            _next = 0
            for c in str_n:
                _next += int(c) ** 2
            n = _next
        return n == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))  # True
    print(s.isHappy(2))  # False

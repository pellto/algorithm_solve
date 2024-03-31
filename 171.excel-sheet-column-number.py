class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        out = 0
        for c in columnTitle[::-1]:
            out += (ord(c) - ord("A") + 1) * base
            base *= 26
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))  # 1
    print(s.titleToNumber("AB"))  # 28
    print(s.titleToNumber("ZY"))  # 701

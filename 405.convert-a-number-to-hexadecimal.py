class Solution:
    def toHex(self, num: int) -> str:
        mapper = "0123456789abcdef"
        if num < 0:
            num = 4294967295 + num + 1
        out = ""
        while 16 <= num:
            out += f"{mapper[num%16]}"
            num //= 16
        out += f"{mapper[num]}"
        return out[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.toHex(26))  # 1a
    print(s.toHex(0))  # 0
    print(s.toHex(-1))  # ffffffff
    print(s.toHex(-2))  # fffffffe

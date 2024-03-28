class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for c in s[::-1]:
            if c != " ":
                cnt += 1
            if c == " " and cnt != 0:
                return cnt
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))  # 5
    print(s.lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print(s.lengthOfLastWord("luffy is still joyboy"))  # 6

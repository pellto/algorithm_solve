class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        if len_s == 1:
            return False
        jump = 0
        while jump < len_s - 1:
            if len_s % (jump + 1) != 0:
                jump += 1
                continue
            idx = jump + 1
            sub = s[: jump + 1]
            all_check = True
            while idx < len_s:
                if sub != s[idx : idx + jump + 1]:
                    all_check = False
                    break
                idx += jump + 1

            if all_check:
                return True
            jump += 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("abab"))  # True
    print(s.repeatedSubstringPattern("aba"))  # False
    print(s.repeatedSubstringPattern("abcabcabcabc"))  # True
    print(s.repeatedSubstringPattern("abcbaabcba"))  # True
    print(s.repeatedSubstringPattern("a"))  # False
    print(s.repeatedSubstringPattern("aa"))  # True

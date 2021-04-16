class Solution:
    def isValid(self, s):
        prev = s
        while len(s) > 0:
            s = s.replace("abc", "")
            if prev == s:
                return False
            prev = s
        return True


if __name__=="__main__":
    print(Solution().isValid("aabcbc"))
    print(Solution().isValid("abcabcababcc"))
    print(Solution().isValid("abccba"))
    print(Solution().isValid("cababc"))

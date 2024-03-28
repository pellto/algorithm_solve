class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opener = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in opener:
                stack.append(opener[c])
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != c:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # true
    print(s.isValid("()[]{}"))  # true
    print(s.isValid("(]"))  # false
    print(s.isValid("("))  # false
    print(s.isValid(")"))  # false

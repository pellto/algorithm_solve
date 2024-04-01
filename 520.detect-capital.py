class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper()
            or word.islower()
            or (word[0].isupper() and word[1:].islower())
        )


if __name__ == "__main__":
    s = Solution()
    print(s.detectCapitalUse("USA"))  # True
    print(s.detectCapitalUse("USa"))  # False
    print(s.detectCapitalUse("g"))  # True
    print(s.detectCapitalUse("Google"))  # True

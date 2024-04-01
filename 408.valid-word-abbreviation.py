class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = abbr_idx = 0
        while abbr_idx < len(abbr):
            if abbr[abbr_idx].isalpha():
                if word_idx >= len(word) or word[word_idx] != abbr[abbr_idx]:
                    return False
                abbr_idx += 1
                word_idx += 1
            else:
                if abbr[abbr_idx] == "0":
                    return False
                substring = ""
                while not abbr[abbr_idx].isalpha():
                    substring += abbr[abbr_idx]
                    abbr_idx += 1
                    if abbr_idx >= len(abbr):
                        return len(word[word_idx:]) == int(substring)
                word_idx += int(substring)
        return len(word) == word_idx


if __name__ == "__main__":
    s = Solution()
    print(s.validWordAbbreviation("internationalization", "i12iz4n"))  # True
    print(s.validWordAbbreviation("apple", "a2e"))  # False
    print(s.validWordAbbreviation("a", "2"))  # False
    print(s.validWordAbbreviation("internationalization", "i5a11o1"))  # True
    print(s.validWordAbbreviation("internationalization", "20"))  # True
    print(s.validWordAbbreviation("a", "01"))  # False
    print(s.validWordAbbreviation("ab", "a"))  # False

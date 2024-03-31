class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()
        if len(s_arr) != len(pattern):
            return False
        word_dict = dict()
        pattern_dict = dict()
        for p, word in zip(pattern, s_arr):
            checker = True
            if p not in pattern_dict:
                pattern_dict[p] = word
                checker = False
                if word in word_dict and word_dict[word] != p:
                    return False
            if word not in word_dict:
                word_dict[word] = p
                checker = False
                if p in pattern_dict and pattern_dict[p] != word:
                    return False
            if checker:
                if pattern_dict[p] != word or word_dict[word] != p:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))  # True
    print(s.wordPattern("baab", "dog cat cat dog"))  # True
    print(s.wordPattern("abba", "dog cat cat fish"))  # False
    print(s.wordPattern("aaaa", "dog cat cat dog"))  # False
    print(s.wordPattern("abba", "dog dog dog dog"))  # False
    print(s.wordPattern("abc", "dog cat dog"))  # False
    print(s.wordPattern("aba", "dog cat cat"))  # False
    print(s.wordPattern("aaa", "aa aa aa aa"))  # False

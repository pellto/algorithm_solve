class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s_arr = list(s)
        idxs = []
        for idx, c in enumerate(s):
            if c in vowels:
                idxs.append(idx)
        for i in range(len(idxs) // 2):
            s_arr[idxs[i]], s_arr[idxs[-i - 1]] = (
                s_arr[idxs[-i - 1]],
                s_arr[idxs[i]],
            )

        return "".join(s_arr)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("hello"))  # "holle"
    print(s.reverseVowels("leetcode"))  # "leotcede"
    print(s.reverseVowels("apple"))  # "eppla"
    print(s.reverseVowels("hi"))  # "hi"
    print(s.reverseVowels("aA"))  # "Aa"

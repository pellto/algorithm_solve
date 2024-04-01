from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_len = len(words)
        for idx, word in enumerate(words):
            if len(word) > max_len:
                return False
            if len(word) < max_len:
                words[idx] = word.ljust(max_len, "_")

        idx, pivot = 0, 0
        while pivot < max_len:
            if words[pivot][idx] != words[idx][pivot]:
                return False
            idx += 1
            if idx == max_len:
                pivot += 1
                idx = pivot
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validWordSquare(["abcd", "bnrt", "crmy", "dtye"]))  # True
    print(s.validWordSquare(["abcd", "bnrt", "crm", "dt"]))  # True
    print(s.validWordSquare(["ball", "area", "read", "lady"]))  # False
    print(s.validWordSquare(["abc", "b"]))  # False

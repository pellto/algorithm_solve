from typing import List


class Solution:
    def shortestDistance(
        self, wordsDict: List[str], word1: str, word2: str
    ) -> int:
        word1_idxs, word2_idxs = [], []
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word1_idxs.append(idx)
            elif word == word2:
                word2_idxs.append(idx)

        min_distance = 3 * 10**4 + 2
        for w1 in word1_idxs:
            for w2 in word2_idxs:
                min_distance = min(min_distance, abs(w2 - w1))
        return min_distance


if __name__ == "__main__":
    s = Solution()
    print(
        s.shortestDistance(
            ["practice", "makes", "perfect", "coding", "makes"],
            "coding",
            "practice",
        )
    )  # 3
    print(
        s.shortestDistance(
            ["practice", "makes", "perfect", "coding", "makes"],
            "makes",
            "coding",
        )
    )  # 1

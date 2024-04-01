from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                rank_dict[s] = "Gold Medal"
            elif i == 1:
                rank_dict[s] = "Silver Medal"
            elif i == 2:
                rank_dict[s] = "Bronze Medal"
            else:
                rank_dict[s] = str(i + 1)

        out = []
        for s in score:
            out.append(rank_dict[s])
        return out


if __name__ == "__main__":
    s = Solution()
    print(
        s.findRelativeRanks([5, 4, 3, 2, 1])
    )  # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

    print(
        s.findRelativeRanks([10, 3, 8, 9, 4])
    )  # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(c) for c in strs])
        ret = ""
        for i in range(min_length):
            base = strs[0][i]
            for c in strs:
                if c[i] != base:
                    return ret
            ret += base
        return ret


if __name__ == "__main__":
    solution = Solution()
    print(
        "#1", solution.longestCommonPrefix(["flower", "flow", "flight"])
    )  # "fl"
    print("#2", solution.longestCommonPrefix(["dog", "racecar", "car"]))  # ""

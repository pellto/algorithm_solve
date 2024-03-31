from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ret = []
        for i in range(len(currentState)):
            start = currentState.find("++", i)
            if start >= 0:
                ret.append(
                    currentState[:start] + "--" + currentState[start + 2 :]
                )
        return list(set(ret))


if __name__ == "__main__":
    s = Solution()
    print(s.generatePossibleNextMoves("++++"))  # ["--++","+--+","++--"]
    print(s.generatePossibleNextMoves("+"))  # []

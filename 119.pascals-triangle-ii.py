from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [[1]]
        it = 2
        while it <= (rowIndex + 1):
            tmp = [1]
            prev = out[it - 2]
            tmp_iter = len(prev) - 1
            idx = 0
            while tmp_iter > 0:
                tmp.append(prev[idx] + prev[idx + 1])
                tmp_iter -= 1
                idx += 1
            tmp.append(1)
            out.append(tmp)
            it += 1
        return out[rowIndex]


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))  # [1, 3, 3, 1]
    print(s.getRow(0))  # [1]
    print(s.getRow(1))  # [1, 1]

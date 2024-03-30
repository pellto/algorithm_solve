from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        it = 2
        while it <= numRows:
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
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(s.generate(1))  # [[1]]

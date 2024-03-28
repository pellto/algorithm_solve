from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cand = []
        for num in nums[::-1]:
            if num == val:
                continue
            cand.append(num)
        cand_idx = 0
        for idx, num in enumerate(nums):
            if num == val:
                nums[idx] = cand[cand_idx] if cand_idx < len(cand) else -1
                cand_idx += 1
        return len(cand)


if __name__ == "__main__":
    s = Solution()
    p1, v1 = [3, 2, 2, 3], 3
    p2, v2 = [0, 1, 2, 2, 3, 0, 4, 2], 2
    print(s.removeElement(p1, v1))  # 2, nums = [2, 2, _, _]
    print("p1 >> ", p1)
    print(s.removeElement(p2, v2))  # 5, nums = [0, 1, 4, 0, 3, _, _, _]
    print("p2 >> ", p2)
    p3, v3 = [2, 3, 3], 3
    print(s.removeElement(p3, v3))
    print("p3 >> ", p3)

    p4, v4 = [2], 3
    print(s.removeElement(p4, v4))  # 1, nums = [2]
    print("p4 >> ", p4)

    p5, v5 = [4, 2, 0, 2, 2, 1, 4, 4, 1, 4, 3, 2], 4
    print(s.removeElement(p5, v5))  # 8, nums = [2, 2, 0, 2, 2, 1, 3, 1, _, _]
    print("p5 >> ", p5)

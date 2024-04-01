class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = list(bin(num)[2:])
        for i, n in enumerate(bin_num):
            if n == "1":
                bin_num[i] = "0"
            else:
                bin_num[i] = "1"
        return int("".join(bin_num), 2)


if __name__ == "__main__":
    s = Solution()
    print(s.findComplement(5))  # 2
    print(s.findComplement(1))  # 0

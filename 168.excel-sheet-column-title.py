class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        convert_dict = {}
        for num in range(65, 91):
            convert_dict[(num - 65 + 1) % 26] = chr(num)

        out = ""
        base = 26
        it = 1
        while columnNumber > 0:
            idx = (columnNumber % base) // it
            out += convert_dict[idx]
            if idx == 0:
                columnNumber -= 26 * it
            else:
                columnNumber -= idx * it
            it *= 26
            base *= 26
        return out[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))  # "A"
    print(s.convertToTitle(28))  # "AB"
    print(s.convertToTitle(701))  # "ZY"

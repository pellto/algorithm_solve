class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        out = []
        r_num1 = num1[::-1]
        r_num2 = num2[::-1]
        it1 = it2 = 0
        carry = 0
        while it1 < len(r_num1) or it2 < len(r_num2):
            n1 = n2 = 0
            if it1 < len(r_num1):
                n1 = int(r_num1[it1])
            if it2 < len(r_num2):
                n2 = int(r_num2[it2])
            v = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            out.append(v)
            it1 += 1
            it2 += 1

        if carry > 0:
            out.append(carry)

        return "".join([str(x) for x in out[::-1]])


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings("11", "123"))  # 134
    print(s.addStrings("456", "77"))  # 533
    print(s.addStrings("0", "0"))  # 0
    print(s.addStrings("1", "9"))  # 10

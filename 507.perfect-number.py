class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 5:
            return False
        divisors = [1]
        div = 2
        while div * div <= num:
            share = num // div
            if share * div == num:
                divisors.append(share)
                if share != div:
                    divisors.append(div)
            div += 1
        return sum(divisors) == num


if __name__ == "__main__":
    s = Solution()
    print(s.checkPerfectNumber(28))  # True
    print(s.checkPerfectNumber(7))  # False
    print(s.checkPerfectNumber(6))  # True

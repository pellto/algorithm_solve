class Solution:
    symbol_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    changeable = {
        "IIIV": 2,
        "IIV": 3,
        "IV": 4,
        "IIIX": 7,
        "IIX": 8,
        "IX": 9,
        "XXXL": 20,
        "XXL": 30,
        "XL": 40,
        "XXXC": 70,
        "XXC": 80,
        "XC": 90,
        "CCCD": 200,
        "CCD": 300,
        "CD": 400,
        "CCCM": 700,
        "CCM": 800,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        ret = 0
        for c in self.changeable:
            cs = s.replace(c, "")
            if s != cs:
                ret += self.changeable[c]
            s = cs
        for c in s:
            ret += self.symbol_map[c]
        return ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))  # 3
    print(solution.romanToInt("LVIII"))  # 58
    print(solution.romanToInt("MCMXCIV"))  # 1994
    print(solution.romanToInt("DCXXI"))  # 621

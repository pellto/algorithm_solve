class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        splitted_s = s.split("-")
        new_arr = []
        reformatting_s = "".join(list(map(lambda x: x.upper(), splitted_s)))
        idx = len(reformatting_s)
        while idx > 0:
            new_arr.append(reformatting_s[max(0, idx - k) : idx])
            idx -= k
        return "-".join(new_arr[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # 5F3Z-2E9W
    print(s.licenseKeyFormatting("2-5g-3-J", 2))  # 2-5G-3J
    print(s.licenseKeyFormatting("2-4A0r7-4k", 4))  # "24A0-R74K"

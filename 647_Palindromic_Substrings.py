class Solution:
    def countSubstrings(self, s):
        """
        Runtime: 556 ms, faster than 12.58%
        Memory Usage: 14.3 MB, less than 53.56%
        """
        answer = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    answer += 1
        return answer


if __name__=="__main__":
    print(Solution().countSubstrings("abc")) # 3
    print(Solution().countSubstrings("aaa")) # 6

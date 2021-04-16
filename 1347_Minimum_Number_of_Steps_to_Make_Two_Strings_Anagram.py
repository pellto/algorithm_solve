class Solution:
    def minSteps(self, s, t):
        s_dict, t_dict = {}, {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 0
            s_dict[c] += 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1

        for c in s_dict:
            if c in t_dict:
                if s_dict[c] - t_dict[c] > 0:
                    s_dict[c] = s_dict[c] - t_dict[c]
                else:
                    s_dict[c] = 0
        return sum(s_dict.values())

if __name__=="__main__":
    print(Solution().minSteps("bab", 'aba'))
    print(Solution().minSteps("leetcode", 'practice'))
    print(Solution().minSteps("anagram", 'mangaar'))
    print(Solution().minSteps("xxyyzz", 'xxyyzz'))
    print(Solution().minSteps("friend", 'family'))
    

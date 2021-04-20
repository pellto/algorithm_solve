class Solution:
    def maxRepOpt1(self, text):
        """
        Runtime: 72 ms, faster than 40.27%
        Memory Usage: 15.6 MB, less than 38.23%
        """
        count_dict = {}
        for i in range(len(text)):
            if text[i] not in count_dict:
                count_dict[text[i]] = 0
            count_dict[text[i]] += 1
        if len(count_dict) == 1:
            return count_dict[text[0]]

        temp = []; i = 0
        while i < len(text):
            j = i + 1
            while j < len(text):
                if text[i] != text[j]:
                    break
                j += 1
            temp.append([text[i], j - i])
            i = j

        res = 0
        for w, c in temp:
            res = max(res, min(c + 1, count_dict[w]))

        for i in range(len(temp) - 2):
            if temp[i][0] == temp[i + 2][0] and temp[i + 1][1] == 1:
                res = max(res, min(temp[i + 2][1] + temp[i][1] + 1, count_dict[temp[i][0]]))

        return res


if __name__=="__main__":
    print(Solution().maxRepOpt1("ababa")) # 3
    print(Solution().maxRepOpt1("aaabaaa")) # 6
    print(Solution().maxRepOpt1("aaabbaaa")) # 4
    print(Solution().maxRepOpt1("aaaaa")) # 5
    print(Solution().maxRepOpt1("abcdef")) # 1

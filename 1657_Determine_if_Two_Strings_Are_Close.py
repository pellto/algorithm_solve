class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        w1_dict, w2_dict = {}, {}
        for w in word1:
            if w not in w1_dict:
                w1_dict[w] = 0
            w1_dict[w] += 1

        for w in word2:
            if w not in w2_dict:
                w2_dict[w] = 0
            w2_dict[w] += 1

        if w1_dict.keys() != w2_dict.keys():
            return False

        return sorted(w1_dict.values()) == sorted(w2_dict.values())


if __name__=="__main__":
    print(Solution().closeStrings("abc", "bca"))
    print(Solution().closeStrings("a", "aa"))
    print(Solution().closeStrings("cabbba", "abbccc"))
    print(Solution().closeStrings("cabbba", "aabbss"))
    

class Solution:
    def arrangeWords(self, text):
        """
        Runtime: 40 ms, faster than 73.50%
        Memory Usage: 15.8 MB, less than 94.33%
        """
        text = " ".join(sorted(text.lower().split(" "), key=lambda x:len(x)))
        return text[0].upper() + text[1:]


if __name__=="__main__":
    # Is cool leetcode
    print(Solution().arrangeWords("Leetcode is cool"))
    # On and keep calm code
    print(Solution().arrangeWords("Keep calm and code on"))
    # To be or to be not
    print(Solution().arrangeWords("To be or not to be"))
    

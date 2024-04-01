from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        out = []
        for word in words:
            for row in rows:
                if len(set(word.lower()) - row) == 0:
                    out.append(word)
                    break
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))  # ["Alaska","Dad"]
    print(s.findWords(["omk"]))  # []
    print(s.findWords(["adsdf", "sfd"]))  # ["adsdf","sfd"]

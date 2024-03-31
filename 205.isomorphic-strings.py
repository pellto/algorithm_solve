class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map = dict()
        t_s_map = dict()
        for sc, tc in zip(s, t):
            if sc in s_t_map:
                if s_t_map[sc] != tc:
                    return False
            if tc in t_s_map:
                if t_s_map[tc] != sc:
                    return False
            s_t_map[sc] = tc
            t_s_map[tc] = sc
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))  # True
    print(s.isIsomorphic("foo", "bar"))  # False
    print(s.isIsomorphic("paper", "title"))  # True

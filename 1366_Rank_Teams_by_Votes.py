class Solution:
    def rankTeams(self, votes):
        ranking = {}
        for vote in votes:
            for i, team in enumerate(vote):
                if team not in ranking:
                    ranking[team] = [0] * len(vote)
                ranking[team][i] -= 1
        return "".join(list(map(str, sorted(ranking, key=lambda x:(ranking[x], x)))))


if __name__=="__main__":
    print(Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    print(Solution().rankTeams(["WXYZ","XYZW"]))
    print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print(Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))

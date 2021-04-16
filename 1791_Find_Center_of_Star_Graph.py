class Solution:
    def findCenter(self, edges):
        cnt_dict = {}
        for edge in edges:
            if edge[0] not in cnt_dict:
                cnt_dict[edge[0]] = 0
            if edge[1] not in cnt_dict:
                cnt_dict[edge[1]] = 0
            cnt_dict[edge[0]] += 1
            cnt_dict[edge[1]] += 1
        return sorted(cnt_dict, key=lambda x:cnt_dict[x])[-1]


if __name__=="__main__":
    print(Solution().findCenter([[1,2],[2,3],[4,2]]))
    print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))

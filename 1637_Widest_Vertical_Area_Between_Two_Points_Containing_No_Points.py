class Solution:
    def maxWidthOfVerticalArea(self, points):
        """
        Runtime: 836 ms, faster than 66.13%
        Memory Usage: 55.3 MB, less than 47.72%
        """
        points = sorted(points, key=lambda x:x[0])
        ret = -1
        for i in range(len(points) - 1):
            ret = max(ret, points[i+1][0] - points[i][0])

        return ret


if __name__=="__main__":
    print(Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]])) # 1
    print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])) # 3

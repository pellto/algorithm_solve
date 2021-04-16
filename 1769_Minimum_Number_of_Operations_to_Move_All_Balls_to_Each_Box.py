class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        ret = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    ret[i] += abs(j-i)
        return ret


if __name__=="__main__":
    print(Solution().minOperations("110"))

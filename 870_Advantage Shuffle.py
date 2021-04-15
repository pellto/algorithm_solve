class Solution:
    def advantageCount(self, A, B):
        out = [0] * len(A)
        A = sorted(A)
        b_index_list = sorted(range(len(A)), key=lambda x:B[x], reverse=True)

        l, r = 0, len(A) - 1
        for i in b_index_list:
            if B[i] >= A[r]:
                out[i] = A[l]
                l += 1
            else:
                out[i] = A[r]
                r -= 1
        return out


if __name__=="__main__":
    print(Solution().advantageCount([2,7,11,15], [1,10,4,11]))
    print(Solution().advantageCount([12,24,8,32], [13,25,32,11]))

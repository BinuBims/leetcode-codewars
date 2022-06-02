class Solution:
    def transpose(matrix):
        m,n=len(matrix),len(matrix[0])
        ans = [[None] * m for _ in range(n)]
        print(ans)
        print(m)
        for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        
        return ans
print(Solution.transpose([[1,2],[4,5]]))
class Solution:
    def editDistance(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)
        dp = [[-1 for _ in range(n2)]for _ in range(n1)]
        def fun(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if dp[i][j] != -1:
                return dp[i][j]
            if str1[i] == str2[j]:
                dp[i][j] = fun(i-1,j-1)
            else:
                dp[i][j] = 1 + min(fun(i-1,j-1), fun(i, j-1), fun(i-1, j))
            return dp[i][j]
            
        return fun(n1-1,n2-1)
           
        # Code here
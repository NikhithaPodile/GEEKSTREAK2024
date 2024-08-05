#User function Template for python3
class Solution:
    from collections import Counter

    def rowWithMax1s(self,arr):
        m = len(arr)
        if m == 0:
            return -1
        n = len(arr[0])
        if n == 0:
            return -1
        maxo = 0
        ans = -1
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) // 2
                if arr[i][mid] == 1:
                    r = mid
                else:
                    l = mid + 1
            if arr[i][l] == 1:
                p = n - l
                if p > maxo:
                    maxo = p
                    ans = i
        return ans
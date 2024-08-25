class Solution:
    def canSplit(self, arr):
        #code here
        s = sum(arr)
        if s&1:
            return False
            
        t = s//2
        for i in arr:
            t-=i
            if t==0:
                return True
            elif t<0:
                return False
        return False
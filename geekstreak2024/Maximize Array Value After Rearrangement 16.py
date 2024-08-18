class Solution:
    def Maximize(self, arr): 
        # Complete the function
        arr.sort()
        sum=0
        for i in range(0,len(arr)):
            sum+=i*arr[i]
        return sum%(10**9+7)
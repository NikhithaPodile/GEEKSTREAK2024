#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        sum=arr1+arr2
        n=sorted(sum)
        return n[k-1]
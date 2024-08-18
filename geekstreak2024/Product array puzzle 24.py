#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
        ans=[]
        if zeros>=2:
            for i in range(len(nums)):
                ans.append(0)
        elif zeros==1:
            product=1
            for i in range(len(nums)):
                if nums[i]!=0:
                    product*=nums[i]
            for i in range(len(nums)):
                if nums[i]!=0:
                    ans.append(0)
                else:
                    ans.append(product)
        else:
            product=1
            for i in range(len(nums)):
                product*=nums[i]
            for i in range(len(nums)):
                ans.append(product//nums[i])
        return ans

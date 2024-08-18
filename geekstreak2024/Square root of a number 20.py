#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n):
        if n == 0 or n == 1:
            return n
    
        low, high = 1, n
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            # If mid*mid is equal to n, then mid is the square root
            if mid * mid == n:
                return mid
            
            # If mid*mid is less than n, then the floor of sqrt(n) must be mid
            if mid * mid < n:
                low = mid + 1
                ans = mid  # update ans since mid could be the floor value
            else:
                high = mid - 1
        
        return ans
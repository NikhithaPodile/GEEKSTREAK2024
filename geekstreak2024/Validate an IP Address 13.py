#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        a = str.split('.')
        c = 0
        
        for i in a :
            if 0 <= int(i) and int(i) <=  255 :
                c +=1
        
        if c == 4 :
            return True 
        return False
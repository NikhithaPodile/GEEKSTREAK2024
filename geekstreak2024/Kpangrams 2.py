#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        alphabet = 0
        for char in string:
            if char.isalpha():
                alphabet += 1
        if alphabet < 26:
            return False
        ch = 'a'
        count = 0
        while(ch <= 'z'):
            if ch not in string:
                count += 1
            ch = chr(ord(ch)+1)
        if count <= k:
            return True
        else:
            return False
    
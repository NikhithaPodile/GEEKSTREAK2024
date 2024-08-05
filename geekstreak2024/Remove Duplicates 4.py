#User function Template for python3
class Solution:
    def removeDups(self, str):
        ans = []
        for ele in str:
            if ele in ans:
                continue
            else:
                ans.append(ele)
            my_string = "".join(ans)
            
        return my_string
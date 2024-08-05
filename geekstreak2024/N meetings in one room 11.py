#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        arr=[]
        for i in range(n):
            arr.append([start[i], end[i]])
        arr.sort(key=lambda x:x[1])
        i=0
        ans=1
        i=0
        for j in range(1,n):
            if arr[j][0]>arr[i][1]:
                ans+=1
                i=j
        return ans
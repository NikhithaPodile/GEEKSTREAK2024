class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        temp=head
        while(temp.next):
            temp=temp.next
        for i in range(k):
            t=head
            head=head.next
            t.next=None
            temp.next=t
            temp=temp.next
        return head
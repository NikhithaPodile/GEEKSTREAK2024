class Node:
    def _init_(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def addOne(self, head):
        head = self.reverse(head)
        curr = head
        carry = 1

        while curr is not None:
            sum_val = curr.data + carry
            carry = sum_val // 10
            curr.data = sum_val % 10
            prev = curr
            curr = curr.next

        if carry > 0:
            prev.next = Node(carry)

        return self.reverse(head)

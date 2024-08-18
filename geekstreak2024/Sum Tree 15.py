#User function Template for python3
class Node:
    def _init_(self, data):
        self.value = data
        self.left = None
        self.right = None

class Solution:
    def is_sum_tree(self, node):
        # code here
        def check_sum_tree(node):
            # An empty tree is a sum tree and sum of an empty tree is 0
            if node is None:
                return True, 0
            
            # A leaf node is also a sum tree and sum of a leaf node is its own value
            if node.left is None and node.right is None:
                return True, node.data
            
            # Recursively check the left and right subtrees
            left_is_sum_tree, left_sum = check_sum_tree(node.left)
            right_is_sum_tree, right_sum = check_sum_tree(node.right)
            
            # The current node is a sum tree if:
            # 1. The left and right subtrees are sum trees
            # 2. The value of the current node is equal to the sum of values of left and right subtrees
            current_is_sum_tree = (left_is_sum_tree and right_is_sum_tree and
                                   node.data == left_sum + right_sum)
            
            # Return whether the current subtree is a sum tree and the sum of the current subtree
            return current_is_sum_tree, left_sum + right_sum + node.data
        
        # Start the check from the root node
        is_sum_tree, _ = check_sum_tree(node)
        return is_sum_tree
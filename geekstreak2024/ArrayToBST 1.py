# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        def convertToBST(left, right):
            if left > right:
                return None

            # Choose the middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convertToBST(left, mid - 1)
            node.right = convertToBST(mid + 1, right)

            return node

        return convertToBST(0, len(nums) - 1)

# Helper function for inorder traversal
def inorder(root, v):
    if root:
        inorder(root.left, v)
        v.append(root.val)  # Correctly use 'val' instead of 'data'
        inorder(root.right, v)

# Example usage
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    root = solution.sortedArrayToBST(nums)

    # Verify the tree with inorder traversal
    v = []
    inorder(root, v)
    
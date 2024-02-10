# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #if there is no rootnode the depth is zero
        if root == None:
            return 0

        # if there is one node with no childnodes the depth should be one
        if root.left == None and root.right == None:
            return 1

        left=0
        right=0

        # explore child states
        if root.left:
            left += self.maxDepth(root.left)+1

        if root.right:
            right += self.maxDepth(root.right)+1
        
        return max(left, right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left == None:#if left is None, choose right 
            return self.minDepth(root.right)+1
        elif root.right == None:#if right is none, choose left
            return self.minDepth(root.left)+1
        else:#if both are not None, choose the less expensive path
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
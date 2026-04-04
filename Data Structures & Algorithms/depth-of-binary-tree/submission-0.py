# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #input: root of tree
        #output: depth of tree

        #recursively traverse left and right
        #if left and right are null then we know it is leaf
        #max between left and right
        #DFS

        #base case
        if not root:
            return 0

        #recursive calls
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth,rightDepth) #+1 accounts for current node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #input is two roots
        #output true if same val and structure otherwise false

        #recursively traverse left and right
        #DFS

        #base case
        #if p and q are null
            #return True

        #if p and q are not null AND p and q have the same values
            #traverse left of p and q
            #traverse right of p and q
        #else
            #return False
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        



        
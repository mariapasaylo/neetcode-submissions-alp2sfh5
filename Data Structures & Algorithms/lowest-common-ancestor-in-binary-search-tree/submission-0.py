# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #input root and two nodes of the tree
        #return the lowest common ancestor of the two nodes

        #1 and 9 return 5
        #7 and 9 return 8
        #3 and 4 return 3 because ancestor can be a descendant

        #traverse recursively
        #bst means that the value of nodes on the left are less than the right

        #base case
        #if root, p or  q are null
        #   return None
        #if max(p,q) < root
        #   traverse left of tree
        #else if min(p,q) > root
        #   traverse right of tree
        #else - the current node is the lca
        #   return root

        if not root or not p or not q:
            return None
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)  
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

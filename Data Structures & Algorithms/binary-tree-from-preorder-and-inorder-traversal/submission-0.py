# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #input list of values to put in the tree
        #output roots? or root?

        #preorder root left right
        #inorder left root right

        #preorder first element of list is head
        #find the index of this node in inorder array
        #inorder we can split the array to get left and right subtree based on where the root is
        #build the tree using DFS
        
        #global variable for inorder index and preorder index initialized at 0
        #dfsHelper(limit)
        #   declare non local variable inIdx and preIdc
        #   if preIndx >= len(preorder)
        #       return None
        #   if inorder[inIndx] == limit #we stop building the left subtree
        #       increment inIdx
        #       return None
        #   create root node where the value is preorder[preIndx]
        #   increment preIdx
        #   recursive call to build left subtree passing in the root.val as the limit
        #   recursive call to build right subtree passing in the limit as the limit
        #   return root
        #return dfsHelper(positive infinity)

        inIndx = 0
        preIndx = 0
        def dfs(limit):
            nonlocal inIndx, preIndx #allows modification outside of this function
            if preIndx >= len(preorder):
                return None
            if inorder[inIndx] == limit:
                inIndx += 1
                return None
            root = TreeNode(preorder[preIndx])
            preIndx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))




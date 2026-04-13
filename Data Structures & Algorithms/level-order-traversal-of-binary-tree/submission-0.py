# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #input: root of a tree
        #list of list each level from left to right [[0],[1,2],[...]]

        #bfs traverse each level
        #use a queue

        #store final result = []

        #create a deque
        #append the root

        #while there queue is not empty
        #   get length of queue
        #   create empty array level to store nodes in the level
        #   for each element in the q
        #       pop the node from the left
        #       if the node exists
        #           append the value to level
        #           append left and right node to the q
        #   if level is not empty
        #       append level to result
        #
        #return res

        result = []

        q = collections.deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result









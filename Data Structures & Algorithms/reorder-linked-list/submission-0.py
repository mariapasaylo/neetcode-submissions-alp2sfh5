# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #input head of linkedlist
        #reorder nodes  0 , n-1, 1, n-2, 2, n-3, ...
        
        #alternating from end to beginning
        #spiral pattern
        #keep track of current
        #recursion

        #recursive function that takes in root and cur
        #   base case is cur not at the end of the list
        #       return root

        #   root = recursive call root and cur.next
        #   if root is not at the end of the list
        #       return None
        #   tmp = None
        #   if root == cur or root.next == cur
        #       cur.next = None
        #   else
        #       update temp to root.next
        #       root.next = cur
        #       cur.next = tmp

        #   return tmp

        #call recursive function with head and head.next 

        def rec(root: ListNode, cur: ListNode) -> ListNode :
            if not cur:
                return root
            
            root = rec(root, cur.next)

            if not root:
                return None
            
            tmp = None

            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            
            return tmp

        head = rec(head, head.next)

        



        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #input: head of list
        #output: true if cycle, else false

        #slow and fast pointer
        #if last element in the node -1 then not cycle

        #iterate through list
        #   if the node points to null 
        #       return false
        # return true

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
        
        
        
        
        
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
        # start both at head

        #while fast and fast.next not null (covers even and odd cases)
        #   advance slow by 1
        #   advance fast by 2
        #   if slow is the same as fast
        #       return True - this means there is a cycle
        #otherwise, return false

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
        
        
        
        
        
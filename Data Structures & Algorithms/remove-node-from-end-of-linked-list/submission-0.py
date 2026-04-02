# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #input: head, n
        #outptut: head w/o nth node from the END of the list

        #dummy node at head
        #two pointer method
        #left at dummy and right at head
        
        #set new node called dummy that points to head
        #point left to dummy
        #point right at head

        #advance the right pointer n times
        #move left and right until right hits null
        ##left is now right before the node we want to delete
        #left.next = left.next.next
        #return dummy.next

        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        
        left.next = left.next.next

        return dummy.next

        
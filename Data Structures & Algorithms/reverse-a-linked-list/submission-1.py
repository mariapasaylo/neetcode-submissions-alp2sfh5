# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #input: head of linkedlist
        #output: head pf reverse linkedlist

        #O(n) time and O(1) space soln by flipping hte pointers

        #initialize curr = head
        #prev = none

        #while current node is not null
        #   temp = next node
        #   set node's next to prev
        #   store prev to be current
        #   current to be the temp

        #return previous

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

        
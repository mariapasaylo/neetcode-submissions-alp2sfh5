# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #input: head of linkedlist
        #output: head pf reverse linkedlist

        #head will be the last

        #tempnode

        #use stack then create new linked list by popping from stack

        #for current in list
        #   insert to stack
        # initialize new list with 
        #while stack not empty
        #   pop stack and assign as next
        
        stack =[]

        if not head:
            return head

        while head:
            stack.append(head.val)
            head = head.next
        
        temp = ListNode(stack.pop())
        res = temp
        while stack:
            temp.next = ListNode(stack.pop())
            temp = temp.next

        return res

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Input: array of k sorted linked lists
        #Output: merged list in ascending order

        #brute force store in array, mergesort, and then create linked list O(nlogn)
        #iteratively pick smallest head node among all lists O(n*k)
        #merge list one by one using pointers O(n*k)
        #head of each list in min heap O(nlogk)
        #recursion divide and conquer split into two halves and merge left anf right O(nlogk)
        #recursion but iteratively merge list 0 and 1 , then 2 and 3 ... O(nlogk)

        #result create dummy node
        #current = result
        #initialize minheap to empty

        #for each list
        #   if list is not empty
        #       push minheap and and tuple(list.val, i, list) into heapq

        #while min heap not empty
        #   pop the tuple with the smallest value from heapq
        #   current.next = node
        #   current = current.next

        #   if node.next
        #       push the minHeap and tuple(node.next.val, i , and node.next) into heapq
        
        #return result.next

        res = ListNode(0)
        cur = res
        minHeap = []

        for i, lst in enumerate(lists):
            if list:
                heapq.heappush(minHeap, (lst.val, i, lst))
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return res.next



        
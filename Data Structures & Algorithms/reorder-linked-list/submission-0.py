# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        queue = list()
        while curr:
            queue.append(curr)
            curr = curr.next

        curr = ListNode()
        left, right = 0, len(queue) - 1
        while left < right:
            curr.next = queue[left]
            curr = curr.next
            curr.next = queue[right]
            curr = curr.next
            left += 1 
            right -= 1  

        if left == right:
            curr.next = queue[right]
            curr = curr.next
        curr.next = None
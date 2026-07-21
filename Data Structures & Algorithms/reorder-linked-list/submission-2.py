# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        curr = fast
        second_list = fast
        while fast:
            tmp = fast.next
            fast.next = prev
            prev = fast
            fast = tmp
        
        curr = head 
        while curr and second_list:
            tmp = curr.next
            curr.next = second_list
            curr = tmp
            tmp = second_list.next
            second_list.next = curr
            second_list = tmp



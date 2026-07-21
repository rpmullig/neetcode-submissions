# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        prev = None
        curr = head
        i = 0 
        while curr and i < (length - n):
            prev = curr
            curr = curr.next
            i += 1
        
        if curr and prev:
            prev.next = curr.next
        elif curr:
            head = curr.next
        else:
            return None
        
        return head
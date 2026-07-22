# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder: int = 0 
        dummyHead: ListNode = ListNode()
        curr = dummyHead
        while l1 and l2:
            value: int = l1.val + l2.val + remainder
            remainder = value // 10
            value = value % 10
            curr.next = ListNode(val=value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value = l1.val + remainder
            remainder = value // 10
            value = value % 10
            curr.next = ListNode(val=value)
            curr = curr.next
            l1 = l1.next

        while l2: 
            value = l2.val + remainder
            remainder = value // 10
            value = value % 10
            curr.next = ListNode(val=value)
            curr = curr.next
            l2 = l2.next

        if remainder:
            curr.next = ListNode(val=remainder)

        return dummyHead.next
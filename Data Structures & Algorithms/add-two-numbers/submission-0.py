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
            if remainder > 0:
                curr.next = l1
                value = l1.val + remainder
                remainder = value // 10
                value = value % 10
                curr.val = value
                l1 = l1.next
            else:
                curr.next = l1
                break

        while l2: 
            if remainder > 0:
                curr.next = l2
                value = l2.val + remainder
                remainder = value // 10
                value = value % 10
                curr.val = value
                l2 = l2.next
            else:
                curr.next = l2
                break

        if remainder:
            curr.next = ListNode(val=remainder)

        return dummyHead.next
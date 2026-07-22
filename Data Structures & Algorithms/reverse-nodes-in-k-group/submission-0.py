# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head: Optional[ListNode], k: int):
        dummyHead = ListNode(next=head)
        prev = None
        curr = head
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        return dummyHead.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        prev_tail = dummyHead
        right = head
        left = head
        i = 0
        while right:
            i += 1
            if i == k:
                new_head = right
                right = right.next
                last_node = self.reverse(left, k)
                prev_tail.next = new_head
                prev_tail = last_node
                last_node.next = right
                left = right
                i = 0 
            else:
                right = right.next


        return dummyHead.next
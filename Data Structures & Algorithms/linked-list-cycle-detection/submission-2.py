# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow: # is compares mermory spot, == does __eq__ which is not defined 
                return True 



        return False
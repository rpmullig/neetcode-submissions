# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# heapq.heapify(x)
# heapq.heappush(heap, item)
# heapq.heappop(heap)


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummyHead = ListNode()
        curr = dummyHead
        heap = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(heap)

        while len(heap) > 0:
            _, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))


        return dummyHead.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes.pop(0 - n)

        if len(nodes) == 0:
            return None
        
        for i, n in enumerate(nodes):
            n.next = None
            if i == 0:
                head = nodes[0]
            else:
                nodes[i - 1].next = n
        
        return head
            
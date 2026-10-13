# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        head = None
        curr = head
        addMore = False
        while curr1 or curr2:
            sums = 0
            if curr1 != None:
                sums += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                sums += curr2.val
                curr2 = curr2.next
            
            if addMore:
                sums += 1
                addMore = False

            if sums > 9:
                addMore = True
                sums = sums - 10
                node = ListNode(sums)    
            else:
                node = ListNode(sums)

            if curr == None:
                head = node
            else:
                curr.next = node
            curr = node  
        
        if addMore:
            node = ListNode(1)
            curr.next = node
    
        return head
        
        
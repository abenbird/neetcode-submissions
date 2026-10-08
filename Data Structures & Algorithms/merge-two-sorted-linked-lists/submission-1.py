# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        curr1, curr2, newHead, currNew = list1, list2, None, None
        while curr1 or curr2:
            if curr1 == None:
                currNew.next = curr2
                break
            if curr2 == None:
                currNew.next = curr1
                break
            if curr1.val < curr2.val:
                if newHead == None:
                    newHead = curr1
                else:   
                    currNew.next = curr1 
                currNew = curr1  
                curr1 = curr1.next
            else:
                if newHead == None:
                    newHead = curr2
                else:   
                    currNew.next = curr2
                currNew = curr2   
                curr2 = curr2.next
        return newHead

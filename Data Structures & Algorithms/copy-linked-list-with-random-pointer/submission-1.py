"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
           
        maps = {}
        curr = head
        currCopy = None
        while curr:
            copy = Node(curr.val)
            maps[curr] = copy
            if currCopy:
                currCopy.next = copy
            currCopy = copy
            curr = curr.next
        curr = head
        while curr:
            maps[curr].random = maps.get(curr.random, None)
            curr = curr.next
        return maps[head]
        


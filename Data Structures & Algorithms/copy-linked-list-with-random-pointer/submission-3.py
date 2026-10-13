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
        randomCopy = None
        while curr:
            if curr in maps:
                copy = maps[curr]
            else:
                copy = Node(curr.val)
                maps[curr] = copy
            if currCopy:
                currCopy.next = copy
            if curr.random:
                if curr.random in maps:
                    copy.random = maps[curr.random]
                else:
                    randomCopy = Node(curr.random.val)
                    maps[curr.random] = randomCopy
                    copy.random = randomCopy
            currCopy = copy
            curr = curr.next
        
        return maps[head]
        


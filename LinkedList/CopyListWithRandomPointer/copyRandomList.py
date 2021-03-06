#!/usr/bin/python
"""
Copy List with Random Pointer 

A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list. 

Definition for singly-linked list with a random pointer.
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return None
        curr = head # insert nodes
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        curr = head # copy random pointer
        while curr:
            newNode = curr.next
            if curr.random: newNode.random = curr.random.next
            curr = newNode.next
        curr = head # saparate the two lists
        newhead = head.next
        while curr:
            newNode = curr.next
            curr.next = newNode.next
            if newNode.next: newNode.next = newNode.next.next
            curr = curr.next
        return newhead

def buildList(arr):
    head = RandomListNode(0)
    curr = head
    for i in arr:
        curr.next = RandomListNode(i)
        curr = curr.next
    return head.next

if __name__=="__main__":
    arr = list(range(1,10))
    head = buildList(arr)
    Solution().copyRandomList(head)
"""
Three steps:
1. Insert new Nodes in between the list. eg. N1->N2->N3...to N1->newN1->N2->newN2...
2. Copy the random pointer. 
3. Saparate the two lists.
"""
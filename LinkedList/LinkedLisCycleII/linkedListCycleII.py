#!/usr/bin/python

# Linked List Cycle II 

#  Given a linked list, return the node where the cycle begins. 
#  If there is no cycle, return null.

# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        if not head: return None
        fast = head
        slow = head
        flag = False
        while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
              if slow == fast:
                  flag = True
                  break
        if not flag: return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next 
        return fast 

    def printList(self,head):
        while head:
            print head.val,
            head = head.next
        print

def buildList(arr):
    head = ListNode(0)
    curr = head
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next

    curr = head.next
    while curr.next:
        curr = curr.next
        if not curr.next:
            curr.next = head.next.next.next.next.next
            break
    return head.next

if __name__=="__main__":
    import random
    #arr = random.sample(range(20),10)
    arr = list(range(10))
    sol = Solution()
    head = buildList(arr)
    #sol.printList(head)
    print sol.detectCycle(head).val    

"""
Firstly let us assume the slow pointer (S) and fast pointer (F) 
start at the same place in a n node circle. S run t steps while F 
can run 2t steps, we want to know what is t (where they meet) , then
just solve:  t mod n = 2t mod n,  we know when t = n, they meet, that 
is the start of the circle.

For our problem, we can consider the time when S enter the loop for 
the 1st time, which we assume k step from the head. At this time, 
the F is already in k step ahead in the loop. When will they meet next time? 
Still solve the function:    
t mod n = (k + 2t) mod n
Finally, when t = (n-k), S and F will meet, 
this is k steps before the start of the loop.

The way to find loop start point after loop detect:
1. Set fast to the head.
2. slow = slow.next, fast = fast.next
3. until they meet, count the steps.
"""
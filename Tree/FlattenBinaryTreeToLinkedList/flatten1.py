#!/usr/bin/python

"""
Flatten Binary Tree to Linked List 

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree, 
each node's right child points to the next node of a pre-order traversal.
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import TreeUtil

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root:
            if not root.left:
                root = root.right
            else:
                tmp = root.left
                while tmp.right: tmp = tmp.right
                tmp.right = root.right
                root.right = root.left
                root.left = None
    

if __name__=="__main__":
    arr = [1,2,5,3,4,'#',6]
    sol = Solution()
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    sol.flatten(root)
    TreeUtil.print_tree_graph(root)

"""
Note that the problem requires in-place operation.The flatten procedure is like:  
cut the left child and set to right, the right child is then linked to somewhere 
behind the left child. Where should it be then?  Actually the right child should 
be linked to the most-right node of the left node. So the algorithm is as follows:
(1) store the right child (we call R)
(2) find the right-most node of left child
(3) set R as the right-most node's right child.
(4) set left child as the right child
(5) set the left child NULL
(6) set current node to current node's right child.
(7) iterate these steps until all node are flattened.
"""
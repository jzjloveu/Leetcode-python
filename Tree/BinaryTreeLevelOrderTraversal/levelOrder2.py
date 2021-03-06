#!/usr/bin/python

"""
Binary Tree Level Order Traversal 

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None: return []
        res, self.L = [], {}
        self.preOrder(root, 0)
        for i in sorted(self.L.keys()):
            res.append(self.L[i])
        return res
     
    def preOrder(self, root, level):
        if level in self.L:
            self.L[level].append(root.val)
        else:
            self.L[level] = [root.val]
        if root.left:
            self.preOrder(root.left, level + 1)
        if root.right:
            self.preOrder(root.right, level + 1)
        return
        


if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [3,9,20,'#','#',15,7]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    TreeUtil.print_tree_level(root);print
    print Solution().levelOrder(root)

"""
Use pre-order traversal first, and store the level number,
then output result.
"""
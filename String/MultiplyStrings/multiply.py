#!/usr/bin/python

"""
Multiply Strings  

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

if __name__=="__main__":
    num1 = '22'
    num2 = '11'
    print Solution().multiply(num1,num2)
 



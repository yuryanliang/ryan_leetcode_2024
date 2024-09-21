""" https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

# The idea is similar to https://leetcode.com/problems/add-two-numbers/
# -- iterate backwards and build the result from the back by adding two last digits while keeping carry in mind.
# In the end, if carry is non-zero we append it to the front.

def addBinary(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    # if a[-1] == '1' and b[-1] == '1':
        
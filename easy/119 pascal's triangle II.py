""" https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

Input: rowIndex = 2
Output: [1,2,1]

Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

def pascal(row_index):
    res = [1] * (row_index + 1)
    for i in range(2, row_index + 1):
        for j in range(i -1 , 0, -1):
            res[j] = res[j]+ res[j - 1]
    return res

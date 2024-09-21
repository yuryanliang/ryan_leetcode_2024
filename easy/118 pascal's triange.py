""" https://leetcode.com/problems/pascals-triangle/
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

def pascal(num_rows):
    tri = [[1]]
    for i in range(1, num_rows):
        row_mid = []
        for j in range(0, i -1):
            val = tri[i-1][j] + tri[i-1][j+1]
            row_mid.append(val)
        row = [1] + row_mid + [1]
        tri.append(row)
    return tri

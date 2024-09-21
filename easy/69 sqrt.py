""" https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

def brute_force(x):
    i = 0
    while i ** 2 < x:
        i += 1
    return i - 1

def binary_search(x):
    l = 0
    r = x
    while l < r:
        mid = (l + r) //2
        if mid ** 2 < x:
            l = mid + 1
        else:
            r = mid
    i = l - 1

    small = i ** 2 -x
    big = (i+1) ** 2 - x
    return i if abs(small) < abs(big) else i + 1

if __name__ == '__main__':
    print(binary_search(8))
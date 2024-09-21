"""https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
def brute_force(num1, m, num2, n):
    i = m -1
    j = n -1
    k = m + n -1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -=1
        k-=1

    while j >= 0:
        nums1[k] = nums2[j]
        j-=1
        k-=1

def iteration(nums1, m, nums2, n):
    i = m -1
    j = n - 1
    k = m + n -1

    while j >=0:
        if i >= 0 and nums1[i]>nums2[j]:
            nums1[k]= nums1[i]
            i -=1
        else:
            nums1[k]= nums1[j]
            j-=1
        k -=1

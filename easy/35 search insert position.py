""" https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

"""
def for_loop(nums, target):
    for i, val in enumerate(nums):
        if val >= target:
            return i
    return len(nums)


def binary_search(nums, target):
    if nums[-1] < target:
        return len(nums)

    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(for_loop(nums, target))
    print(binary_search(nums, target))

""" https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""
def brute_force(nums):
    import sys
    max_sum = -sys.maxsize
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            max_sum = max(max_sum, sum(nums[i:j]))
    return max_sum

def best(nums):
    new_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        new_sum = max(nums[i], new_sum + nums[i])
        max_sum = max(max_sum, new_sum)
    return max_sum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(brute_force(nums))
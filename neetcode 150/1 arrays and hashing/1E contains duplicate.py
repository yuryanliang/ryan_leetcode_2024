# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false

def hasDuplicate(nums):
    lookup = set()
    for n in nums:
        if n in lookup:
            return True
        lookup.add(n)
    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    print(hasDuplicate(nums))
    nums =  [1, 2, 3, 4]
    print(hasDuplicate(nums))

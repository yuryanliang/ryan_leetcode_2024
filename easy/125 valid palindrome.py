"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
def is_palindrome(s):
    temp = ''
    for c in s:
        if c.isalpha() or c.isdigit():
            temp += c
    temp = temp.lower()

    l = 0
    r = len(temp) -1

    while l < r:
        if temp[l] != temp[r]:
            return False
        l +=1
        r -= 1
    return True
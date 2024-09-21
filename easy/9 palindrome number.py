"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
def pali_str(x):
    x_str = str(x)
    x_str_rev = x_str[::-1]
    return x_str == x_str_rev
def pali(x):
    if x < 0:
        return False
    res = 0
    n = x
    while n:
        res = res * 10 + n %10
        n= n//10
    return res == x


if __name__ == "__main__":
    print(pali_str(121))
    print(pali_str(-121))
    print(pali(121))
    print(pali(-123))
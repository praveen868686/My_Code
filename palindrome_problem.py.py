# x = 121
# Output: true
# Example 2:
#
x = 1331
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:
#
# Input: x = -101
# Output: false

def isPalindrome(x):
    new_str = reversed(str(x))
    reversed_str = ""
    for i in new_str:
        reversed_str += i
    if reversed_str == str(x):
        return True
    else:
        return False





isPalindrome(x)

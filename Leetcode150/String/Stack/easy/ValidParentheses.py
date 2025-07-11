"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from collections import deque
from itertools import filterfalse


class Solution(object):
    def isValid(self, s):

        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

    def main(self):
        # print(self.isValid("()"))
        print(self.isValid("()[]{}"))
        # print(self.isValid("(]"))
        # print(self.isValid("([])"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

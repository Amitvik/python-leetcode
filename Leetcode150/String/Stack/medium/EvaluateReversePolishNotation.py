"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for i, token in enumerate(tokens):
            if self.is_num(token):
                stack.append(int(token))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                result = self.perform_operation(num1, num2, token)
                stack.append(result)
        return stack[0]

    def perform_operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return int(num1 / num2)

    def is_num(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def main(self):
        print(self.evalRPN(tokens=["2", "1", "+", "3", "*"]))
        print(self.evalRPN(tokens=["4", "13", "5", "/", "+"]))
        print(self.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
        print(self.evalRPN(tokens=["18"]))
        print(self.evalRPN(tokens=["0", "3", "/"]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

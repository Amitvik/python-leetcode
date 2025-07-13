"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104


Follow up: Could you write a solution that works in logarithmic time complexity?
"""
from math import factorial


class Solution:
    def trailingZeroes(self, n: int) -> int:


        fact = 1
        for i in range(2,n+1):
            fact *= i

        count = 0
        while fact %10 == 0:
            count+=1
            fact //=10
        return count

    def main(self):
        print(self.trailingZeroes(n=3))
        print(self.trailingZeroes(n=5))
        print(self.trailingZeroes(n=0))
        print(self.trailingZeroes(n=1574))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

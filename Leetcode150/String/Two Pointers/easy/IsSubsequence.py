"""
392. Is Subsequence
Solved
Easy
Topics
conpanies icon
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
from operator import truediv


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while t_index < len(t) and s_index < len(s):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        if s_index >= len(s):
            return True

        return False

    def main(self):
        print(self.isSubsequence(s = "abc", t = "ahbgdc"))
        print(self.isSubsequence(s = "axc", t = "ahbgdc"))



if __name__ == "__main__":
    sol = Solution()
    sol.main()

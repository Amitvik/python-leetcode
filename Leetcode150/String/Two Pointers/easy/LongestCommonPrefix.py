"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        i = 1
        while i < len(strs):
            word = strs[i]
            min_len = min(len(prefix), len(word))
            prefix = prefix[:min_len]
            j = len(prefix) - 1
            while j >= 0:
                if prefix[j] !=word[j]:
                    prefix = prefix[:j]
                j -= 1

            i += 1

        return prefix

    def main(self):
        print(self.longestCommonPrefix(strs=["flower", "flow", "flight"]))
        print(self.longestCommonPrefix(strs=["dog", "racecar", "car"]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

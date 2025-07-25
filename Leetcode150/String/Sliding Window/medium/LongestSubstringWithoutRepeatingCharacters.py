"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left: int = 0
        longest: int = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(longest, right - left + 1)

        return longest

    def main(self):
        print(self.lengthOfLongestSubstring(s="abcabcbb"))
        print(self.lengthOfLongestSubstring(s="bbbbb"))
        print(self.lengthOfLongestSubstring(s="pwwkew"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

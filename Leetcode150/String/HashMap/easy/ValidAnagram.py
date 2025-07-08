"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict: dict = {}
        t_dict: dict = {}
        i: int = 0
        if len(s) != len(t): return False
        while i < len(s):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) - 1
            i += 1

        return s_dict == t_dict

    def main(self):
        print(self.isAnagram(s="anagram", t="nagaram"))
        print(self.isAnagram(s="rat", t="car"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        i: int = 0
        char_dict_s: dict = {}
        char_dict_t : dict = {}
        if len(s) != len(t):
            return False
        while i < len(s):

            if s[i] in char_dict_s:
                if t[i] != char_dict_s[s[i]]:
                    return False
            elif t[i] in char_dict_t:
                if char_dict_t[t[i]] != s[i]:
                    return False
            else:
                char_dict_s[s[i]] = t[i]
                char_dict_t[t[i]] = s[i]
            i += 1

        return True

    def main(self):
        print(self.isIsomorphic(s="egg", t="add"))
        print(self.isIsomorphic(s="foo", t="bar"))
        print(self.isIsomorphic(s="paper", t="title"))
        print(self.isIsomorphic(s="badc", t="baba"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

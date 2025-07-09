"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstructEfficient(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        alphabet_count = [0] * 26  # For 'a' to 'z'

        for c in magazine:
            alphabet_count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            idx = ord(c) - ord('a')
            if alphabet_count[idx] == 0:
                return False
            alphabet_count[idx] -= 1

        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}

        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1

        for char in ransomNote:
            if char_count.get(char, 0) == 0:
                return False
            char_count[char] -= 1

        return True

    def canConstructInefficient(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict: dict = {}
        mag_dict: dict = {}
        i: int = 0
        if len(magazine) < len(ransomNote):
            return False
        while i < len(magazine):
            if i < len(ransomNote):
                ransom_dict[ransomNote[i]] = ransom_dict.get(ransomNote[i], 0) + 1
            mag_dict[magazine[i]] = mag_dict.get(magazine[i], 0) + 1
            i += 1

        for key, value in ransom_dict.items():
            if key not in mag_dict or mag_dict.get(key) < value:
                return False

        return True

    def main(self):

        print(self.canConstruct(ransomNote="a", magazine="b"))
        print(self.canConstruct(ransomNote="aa", magazine="ab"))
        print(self.canConstruct(ransomNote="aa", magazine="aab"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

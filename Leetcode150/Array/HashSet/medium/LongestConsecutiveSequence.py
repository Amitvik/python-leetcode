"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        num_set = set(nums)
        if len(num_set) <= 1: return len(num_set)


        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                max_streak = max(current_streak, max_streak)

        return max_streak

    def main(self):
        print(self.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
        print(self.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        print(self.longestConsecutive(nums=[0]))
        print(self.longestConsecutive([0,0]))
        print(self.longestConsecutive([-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

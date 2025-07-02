"""
45. Jump Game II
Solved
Medium
Topics
conpanies icon
Companies
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        min_jump = 0
        end = 0
        if len(nums) - 1 == 0: return 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return 0

            max_reach = max(max_reach, i + nums[i])
            if i == end:
                min_jump+=1
                end = max_reach
                if end >=len(nums)-1: return min_jump

        return min_jump

    def main(self):
        # print(self.jump([1]))
        print(self.jump([1,2,1,1,1]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()

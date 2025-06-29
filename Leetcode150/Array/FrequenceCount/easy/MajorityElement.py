"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate : int = nums[0]
        counter : int = 0
        for num in nums:
            if num == candidate:
                counter+=1
            else:
                if counter <= 0:
                    candidate = num
                    counter += 1
                else:
                    counter-=1

        return candidate


    def main(self):
        print(self.majorityElement(nums = [3,2,3]))
        print(self.majorityElement([1,3,1,1,4,1,1,5,1,1,6,2,2]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()


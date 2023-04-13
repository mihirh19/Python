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
    def majorityElemen2(self, nums: List[int]) -> int:
        num = sorted(nums)
        return num[len(num) // 2]

    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums) // 2
        set_n = set(nums)
        for ele in set_n:
            if nums.count(ele) > x:
                return ele


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums2))
    nums3 = [1, 4, 5, 1, 4, 5, 1, 4, 5, 5, 5, 5, 5]
    print(Solution().majorityElement(nums3))

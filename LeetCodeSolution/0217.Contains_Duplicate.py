"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

"""
Solution:

from the concept of set in python

set have unique elements

so convert list to set and check both length

if the length is same then no duplicate elements


"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    n = [1, 2, 3, 1]
    n2 = [1, 2, 3, 4]
    n3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    s = Solution()
    print(s.containsDuplicate(n))
    print(s.containsDuplicate(n2))
    print(s.containsDuplicate(n3))

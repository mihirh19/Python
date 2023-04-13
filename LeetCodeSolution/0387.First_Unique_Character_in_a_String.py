"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        count = collections.Counter(s)

        for i, val in enumerate(s):
            if count[val] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = "leetcode"
    print(Solution().firstUniqChar(s))

    s2 = "loveleetcode"
    print(Solution().firstUniqChar(s2))

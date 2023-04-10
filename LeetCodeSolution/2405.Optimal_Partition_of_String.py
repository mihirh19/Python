"""Given a string s, partition the string into one or more substrings such that the characters in each substring are
unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.



Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").


Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
"""


class Solution:

    def __init__(self):
        self.substring = None
        self.count = None
        self.last = None

    def partitionString(self, s: str) -> int:
        self.last = [-1] * 26
        self.count = 1
        self.substring = 0

        for i in range(len(s)):
            if self.last[ord(s[i]) - ord('a')] >= self.substring:
                self.count += 1
                substring = i
            self.last[ord(s[i]) - ord('a')] = i

        return self.count


if __name__ == "__main__":
    s = "abacaba"
    print(Solution().partitionString(s))

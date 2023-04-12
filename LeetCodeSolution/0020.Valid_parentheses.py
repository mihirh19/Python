"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in par.keys():
                stack.append(c)

            elif c in par.values():
                if len(stack) == 0 or par[stack.pop()] != c:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    print(s.isValid(s1))
    print(s.isValid(s2))
    print(s.isValid(s3))

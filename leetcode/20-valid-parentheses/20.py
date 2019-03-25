# https://leetcode.com/problems/valid-parentheses/
#
# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#     Input: "()"
#     Output: true
#
# Example 2:
#
#     Input: "()[]{}"
#     Output: true
#
# Example 3:
#
#     Input: "(]"
#     Output: false
#
# Example 4:
#
#     Input: "([)]"
#     Output: false
#
# Example 5:
#
#     Input: "{[]}"
#     Output: true

class Solution:
    # t:O(n), s:O(n)
    def isValid(self, s):
        """Return True is parentheses are correctly laid out in given string,
        False otherwise.

        >>> Solution().isValid('()')
        True
        >>> Solution().isValid('()[]{}')
        True
        >>> Solution().isValid('(]')
        False
        >>> Solution().isValid('([)]')
        False
        >>> Solution().isValid('{[]}')
        True
        >>> Solution().isValid('{')
        False
        >>> Solution().isValid('')
        True
        """
        stack = list()
        mapping = {closing: opening for opening, closing in ('()', '[]', '{}')}
        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
        return not stack

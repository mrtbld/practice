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

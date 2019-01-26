# https://leetcode.com/problems/minimum-window-substring/description/
#
# 76. Minimum Window Substring
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#     Input: S = "ADOBECODEBANC", T = "ABC"
#     Output: "BANC"
#
# Note:
#
# - If there is no such window in S that covers all characters in T, return the
#   empty string "".
# - If there is such window, you are guaranteed that there will always be only
#   one unique minimum window in S.
from collections import Counter, defaultdict

class Solution:
    # t:O(n), s:O(1)
    def minWindow(self, s, t):
        """Return the minimum window of s that contains all chars of t.

        >>> Solution().minWindow('ADOBECODEBANC', 'ABC')
        'BANC'
        >>> Solution().minWindow('abcdefg', 'ag')
        'abcdefg'
        >>> Solution().minWindow('abcdefg', 'c')
        'c'
        >>> Solution().minWindow('abcdefg', 'cc')
        ''
        >>> Solution().minWindow('abbbbabbbabbabaa', 'aa')
        'aa'
        """
        if not s or not t:
            return ''
        min_window = None
        i = j = 0
        l = len(s)
        c = Counter(t)
        window_c = defaultdict(int)
        window_c[s[0]] += 1
        while j < l:
            if c - Counter(window_c):
                j += 1
                if j < l:
                    window_c[s[j]] += 1
            else:
                if min_window is None or j - i < min_window[1] - min_window[0]:
                    min_window = (i, j)
                window_c[s[i]] -= 1
                i += 1
        if min_window is None:
            return ''
        return s[min_window[0]:min_window[1] + 1]

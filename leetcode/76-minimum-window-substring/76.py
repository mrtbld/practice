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
        >>> Solution().minWindow('abbbbabbbabbabaa'*100000, 'aa')
        'aa'
        """
        if not s or not t:
            return ''
        min_window = None
        i = 0
        j = -1
        l = len(s)
        c = defaultdict(int, Counter(t))
        required = len(c)
        window_c = defaultdict(int)
        while j < l:
            if required:
                j += 1
                if j < l:
                    window_c[s[j]] += 1
                    if window_c[s[j]] == c[s[j]]:
                        required -= 1
            else:
                if min_window is None or j - i < min_window[1] - min_window[0]:
                    min_window = (i, j)
                if window_c[s[i]] == c[s[i]]:
                    required += 1
                window_c[s[i]] -= 1
                i += 1
        if min_window is None:
            return ''
        return s[min_window[0]:min_window[1] + 1]

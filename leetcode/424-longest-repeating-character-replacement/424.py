from collections import defaultdict

class Solution:
    # t:O(n), s:O(1)
    def characterReplacement(self, s, k):
        """Returns the length of the longest almost-same-char substring with at
        most k different chars.

        >>> Solution().characterReplacement('ABAB', 2)
        4
        >>> Solution().characterReplacement('AABABBA', 1)
        4
        >>> Solution().characterReplacement('', 1)
        0
        >>> Solution().characterReplacement('ABAB', 0)
        1
        >>> Solution().characterReplacement('ABAB', 1)
        3
        >>> Solution().characterReplacement('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*4, 0)
        1
        >>> Solution().characterReplacement('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*4, 104)
        104
        >>> Solution().characterReplacement('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*4, 100)
        104
        >>> Solution().characterReplacement('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*4, 99)
        103
        >>> Solution().characterReplacement('ABBBACCCADDDAEEEAE', 1)
        5
        >>> Solution().characterReplacement('ABBBACCCADDDAEEEAE', 2)
        6
        >>> Solution().characterReplacement('ABBBA', 2)
        5
        """
        max_len = 0
        counts = defaultdict(int)
        i = j = 0
        l = len(s)
        while j < l:
            length = j - i + 1
            counts[s[j]] += 1
            if length - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
            else:
                max_len = max(max_len, length)
            j += 1
        return max_len

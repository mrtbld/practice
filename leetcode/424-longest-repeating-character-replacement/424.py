# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# 424. Longest Repeating Character
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
# Example 1:
#
#     Input:
#     s = "ABAB", k = 2
#
#     Output:
#     4
#
#     Explanation:
#     Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
#
#     Input:
#     s = "AABABBA", k = 1
#
#     Output:
#     4
#
#     Explanation:
#     Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#     The substring "BBBB" has the longest repeating letters, which is 4.
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

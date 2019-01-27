# https://leetcode.com/problems/longest-palindromic-substring/
#
# 5. Longest Palindromic Substring
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#     Input: "babad"
#     Output: "bab"
#     Note: "aba" is also a valid answer.
#
# Example 2:
#
#     Input: "cbbd"
#     Output: "bb"
from collections import defaultdict

class Solution:
    # t:O(n²), s:O(n²)
    def longestPalindrome(self, s):
        """
        >>> Solution().longestPalindrome('babad')
        'bab'
        >>> Solution().longestPalindrome('cbbd')
        'bb'
        >>> Solution().longestPalindrome('babcdcbabc')
        'babcdcbab'
        >>> Solution().longestPalindrome('abcdcbabcdcb')
        'bcdcbabcdcb'
        >>> Solution().longestPalindrome('abcdcbabcdcbzxxzzxxzzxxzzxxzzxxzzxxzzxxzzxxzmnm')
        'zxxzzxxzzxxzzxxzzxxzzxxzzxxzzxxz'
        >>> Solution().longestPalindrome('aacdefcaa')
        'aa'
        """
        if not s:
            return ''

        char_indexes = defaultdict(list)
        for i, c in enumerate(s):
            char_indexes[c].append(i)

        m = dict()
        def is_palindrome(i, j):
            t = (i, j)
            if t not in m:
                m[t] = i >= j or (s[i] == s[j] and is_palindrome(i+1, j-1))
            return m[t]

        # index, length
        max_plalindrome_pos = (0, 0)
        i = 0
        for i, a in enumerate(s):
            for j in reversed(char_indexes[a]):
                length = j - i + 1
                if max_plalindrome_pos[1] >= length:
                    break
                if is_palindrome(i, j):
                    max_plalindrome_pos = (i, length)
        max_i, max_l = max_plalindrome_pos
        return s[max_i:max_i + max_l]

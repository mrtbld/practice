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
    # t:O(n³), s:O(n)
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
        """
        if not s:
            return ''

        char_indexes = defaultdict(list)
        for i, c in enumerate(s):
            char_indexes[c].append(i)

        # index, length
        max_plalindrome_pos = (0, 0)
        i = 0
        for i, a in enumerate(s):
            for j in reversed(char_indexes[a]):
                length = j - i + 1
                if max_plalindrome_pos[1] >= length:
                    break
                ii = i
                jj = j
                is_palindrome = True
                while ii < jj:
                    if s[ii] != s[jj]:
                        is_palindrome = False
                        break
                    ii += 1
                    jj -= 1
                if is_palindrome:
                    max_plalindrome_pos = (i, length)
        max_i, max_l = max_plalindrome_pos
        return s[max_i:max_i + max_l]

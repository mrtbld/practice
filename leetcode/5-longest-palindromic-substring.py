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

class Solution:
    # t:O(n²), s:O(1)
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

        max_plalindrome_pos = (0, 0)
        i = 0
        for i in range(len(s)):
            for ii, jj in ((i, i), (i, i + 1)):
                while ii >= 0 and jj < len(s) and s[ii] == s[jj]:
                    ii -= 1
                    jj += 1
                length = jj - ii - 1
                if max_plalindrome_pos[1] < length:
                    max_plalindrome_pos = (ii + 1, length)
        max_i, max_l = max_plalindrome_pos
        return s[max_i:max_i + max_l]

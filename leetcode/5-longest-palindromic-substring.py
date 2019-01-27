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
    # t:O(n), s:O(n)
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

        xs = ['_']
        for c in s:
            xs.append(c)
            xs.append('_')

        p = [0] * len(xs)

        longest_center = 0

        # "Current": largest enclosing palindrome.
        current_center = 0
        current_right = 0

        i = 0
        for i in range(len(xs)):
            j = 1
            if i <= current_right:
                right_margin = current_right - i
                mirror = current_center - (i - current_center)
                if p[mirror] < right_margin:
                    # Mirror palindrome, contained within current one.
                    p[i] = p[mirror]
                    continue
                if right_margin == len(xs) - 1:
                    # Mirror palindrome, contained within current one (because
                    # at the end).
                    p[i] = right_margin
                    continue
                if p[mirror] == right_margin:
                    # Mirror palindrome, suffix of current one.
                    j = p[mirror] + 1
                elif p[mirror] > right_margin:
                    # Mirror palindrome, extending outside current one.
                    j = right_margin + 1
            while i - j >= 0 and i + j < len(xs) and xs[i - j] == xs[i + j]:
               j += 1
            p[i] = j - 1
            right = i + p[i]
            if right > current_right:
                current_center = i
                current_right = right
            if p[i] > p[longest_center]:
                longest_center = i
        return s[
            (longest_center - p[longest_center]) // 2
            :(longest_center + p[longest_center]) // 2
        ]

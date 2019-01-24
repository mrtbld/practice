# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# 3. Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
#     Input: "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
#     Input: "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
#     Input: "pwwkew"
#     Output: 3
#     Explanation: The answer is "wke", with the length of 3.
#     Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    # t:O(n), s:O(1) (because char range is constant)
    def lengthOfLongestSubstring(self, s):
        """Return the longest substring with unique characters.

        >>> Solution().lengthOfLongestSubstring('abcabcbb')
        3
        >>> Solution().lengthOfLongestSubstring('bbbbb')
        1
        >>> Solution().lengthOfLongestSubstring('pwwkew')
        3
        >>> Solution().lengthOfLongestSubstring('abc')
        3
        >>> Solution().lengthOfLongestSubstring('a')
        1
        >>> Solution().lengthOfLongestSubstring('')
        0
        >>> Solution().lengthOfLongestSubstring('abacd')
        4
        """

        seen = set()
        substring_start_i = 0
        max_substring_length = 0
        i = 0
        while i < len(s):
            if s[i] in seen:
                seen = set()
                substring_start_i = substring_start_i + 1
                i = substring_start_i
            max_substring_length = max(max_substring_length, i - substring_start_i + 1)
            seen.add(s[i])
            i += 1
        return max_substring_length

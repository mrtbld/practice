class Solution:
    # t:O(n), s:O(1)
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
        >>> Solution().lengthOfLongestSubstring('abcdefcghijklmn')
        12
        >>> Solution().lengthOfLongestSubstring('abcdefcghijklmnd')
        12
        """

        seen_index = dict()
        substring_start_i = 0
        max_substring_length = 0
        i = 0
        while i < len(s):
            if s[i] in seen_index and seen_index[s[i]] >= substring_start_i:
                substring_start_i = seen_index[s[i]] + 1
            max_substring_length = max(max_substring_length, i - substring_start_i + 1)
            seen_index[s[i]] = i
            i += 1
        return max_substring_length

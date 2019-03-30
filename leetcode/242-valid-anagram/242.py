class Solution:
    # t:O(n+m), s:O(k), where n is len(s), m len(t) and k size of alphabet
    def isAnagram(self, s, t):
        """Return True if s an t are anagrams, False otherwise.

        >>> Solution().isAnagram('anagram', 'nagaram')
        True
        >>> Solution().isAnagram('rat', 'car')
        False
        >>> Solution().isAnagram('aaa', 'aaa')
        True
        >>> Solution().isAnagram('a', 'a')
        True
        >>> Solution().isAnagram('', '')
        True
        >>> Solution().isAnagram('a', '')
        False
        >>> Solution().isAnagram('', 'a')
        False
        >>> Solution().isAnagram('aaaa', 'aaa')
        False
        >>> Solution().isAnagram('aaa', 'aaaa')
        False
        >>> Solution().isAnagram('aaba', 'aaa')
        False
        >>> Solution().isAnagram('aaa', 'aaba')
        False
        """
        if len(s) != len(t):
            return False
        t_counts = dict()
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1
        for c in s:
            count = t_counts.get(c, 0)
            if count == 0:
                return False
            t_counts[c] = count - 1
        return True

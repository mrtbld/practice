from collections import defaultdict

class Solution:
    # t:O(nk), s:O(nk), where k is the max length of given strings
    def groupAnagrams(self, strs):
        """Group anagrams of given array of strings.

        >>> Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        offset = ord('a')
        groups = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - offset] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())

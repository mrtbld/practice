# https://leetcode.com/problems/group-anagrams/
#
# 49. Group Anagrams
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#     Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#     Output:
#     [
#       ["ate","eat","tea"],
#       ["nat","tan"],
#       ["bat"]
#     ]
#
# Note:
#
# - All inputs will be in lowercase.
# - The order of your output does not matter.
from collections import defaultdict

class Solution:
    # t:O(n×k×log(k)), s:O(n×k), where k is the max length of given strings
    def groupAnagrams(self, strs):
        """Group anagrams of given array of strings.

        >>> Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

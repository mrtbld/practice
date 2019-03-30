class Solution:
    # t:O(n), s:O(n)
    def longestConsecutive(self, nums):
        """Return the length of the longest consecutive sequence of given array.

        >>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
        4
        >>> Solution().longestConsecutive([0])
        1
        >>> Solution().longestConsecutive([])
        0
        >>> Solution().longestConsecutive([1, 1, 2, 2, 3, 3])
        3
        >>> Solution().longestConsecutive(list(range(-10000, 10000)))
        20000
        >>> Solution().longestConsecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645])
        3
        """

        # Leverage hash table constant lookups by turning the list into a set.
        # Then find the sequences starts, i.e. numbers that don't have their N-1
        # in the set. Then for each sequence, get the length by incrementing the
        # starting number as long as the N+1 is in the set. Keep max of those
        # lengths.
        #
        # This is inspired from graph representation of the problem. The set is
        # equivalent to forward and backward adjacency lists of the directed
        # graph in which each node is a number from the list and each edge
        # points to the next number sequentially (i.e. N+1). Each sequence of
        # the list is then a connected component of the graph and the question
        # becomes which one of them has the most nodes.
        #
        # The problem particularities is that there's either zero or one
        # neighbor, i.e. the graph components are linked lists, thus DFS or BFS
        # traversal are not needed; and that which node is the neighbor is know
        # from the node value itself: N+1; there's no need to store that info.
        # Thus real adjacency lists are unneeded and replaced by (N + 1 in set)
        # or (N - 1 in set) for finding forward and backward neighbors,
        # respectively.

        max_length = 0
        numset = set(nums) # t:O(n), s:O(n)
        seq_starts = (n for n in nums if n - 1 not in numset)
        for start in seq_starts: # t:O(seq_count × avg(seq_size)) = t:O(n)
            end = start
            while end + 1 in numset: # t:O(seq_size)
                end = end + 1
            max_length = max(max_length, end - start + 1)
        return max_length

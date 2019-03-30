from math import ceil

class Solution:
    def countSubstrings(self, s):
        """
        >>> Solution().countSubstrings("abc")
        3
        >>> Solution().countSubstrings("aaa")
        6
        >>> Solution().countSubstrings("abcbabcdcba")
        18
        """
        if not s:
            return ''

        xs = ['_']
        for c in s:
            xs.append(c)
            xs.append('_')

        p = [0] * len(xs)

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
        return sum(ceil(a / 2) for a in p)

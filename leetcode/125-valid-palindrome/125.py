class Solution:
    # t:O(n), s:O(1)
    def isPalindrome(self, s):
        """Return True if given string is a palindrome, False otherwise.
        Only consider ASCII alphanumeric chars, case-insensitively.

        >>> Solution().isPalindrome('A man, a plan, a canal: Panama')
        True
        >>> Solution().isPalindrome('race a car')
        False
        >>> Solution().isPalindrome('')
        True
        >>> Solution().isPalindrome('!?')
        True
        >>> Solution().isPalindrome('a')
        True
        >>> Solution().isPalindrome('abcba')
        True
        >>> Solution().isPalindrome('abccba')
        True
        >>> Solution().isPalindrome('abcdba')
        False
        """
        i = 0
        j = len(s) - 1
        while i < j:
            a = s[i].lower()
            if not ('a' <= a <= 'z' or '0' <= a <= '9'):
                i += 1
                continue
            b = s[j].lower()
            if not ('a' <= b <= 'z' or '0' <= b <= '9'):
                j -= 1
                continue
            if a != b:
                return False
            i += 1
            j -= 1
        return True

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        ones = 0
        while s != "":
            char = s[0]
            curr = s.count(char)
            if curr == 1:
                ones = 1
            else:
                if curr % 2 == 1:
                    ones = 1
                count += curr // 2
            s = s.replace(char, "")
        return count*2 + ones
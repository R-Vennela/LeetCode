class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for char in s:
            if not result:
                result.append(char)
            elif result[-1].isupper() and result[-1].lower() == char:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == char:
                result.pop()
            else:
                result.append(char)
        return "".join(result)
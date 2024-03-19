class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """  
        left = right = 0

        while right < len(chars):
            charCnt = 0
            curChar = chars[right]
            while right < len(chars) and chars[right] == curChar:
                charCnt += 1
                right += 1

            chars[left] = curChar
            left += 1
            if charCnt >= 10:
                count = list(str(charCnt))
                chars[left : left + len(count)] = count
                left += len(count)
            elif charCnt > 1:
                chars[left] = str(charCnt)
                left += 1
        return left  
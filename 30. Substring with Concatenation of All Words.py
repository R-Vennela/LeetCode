class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        n = len(words[0])
        for i in range(n):
            count = words[:]
            for r in range(i,len(s), n):
                if s[r:r+n] in words:
                    while not(s[r:r+n] in count):
                        count.append(s[i:i+n])
                        i+=n
                    count.remove(s[r:r+n])
                    if(len(count) == 0):
                        ans.append(i)
                else:
                    i = r+n
                    count[:] = words[:]
        return ans
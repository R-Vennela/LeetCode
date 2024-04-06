class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_val = 0
        posinds = []
        for i, c in enumerate(s):
            if c == '(':
                current_val += 1
                posinds.append(i)
            elif c == ')':
                current_val -= 1
                if current_val < 0:
                    s = s[:i] + '_' + s[i+1:]
                    current_val += 1
                else:
                    posinds.pop(0)
        for i in posinds:
            s = s[:i] + '_' + s[i+1:]
        s = s.replace('_', '')
        return s
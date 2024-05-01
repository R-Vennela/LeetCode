class Solution:
    def reversePrefix(self, word, ch) :
        r=word.find(ch)
        if r==-1: return word
        s=list(word[:r+1])
        t=list(word[r+1:])
        s.reverse()
        return "".join(s+t)
class Solution:
    def __init__(self):
        self.results = []
        self.dict = set()
    
    def wordBreak(self, s, wordDict) :
        self.results = []
        self.dict = set(wordDict)
        self.backTrack(s, 0, [])
        return self.results
    
    def backTrack(self, s, start, currentSentence):
        if start == len(s):
            self.results.append(" ".join(currentSentence))
            return
        for i in range(start, len(s)):
            if s[start:i+1] in self.dict:
                currentSentence.append(s[start:i+1])
                self.backTrack(s, i + 1, currentSentence)
                currentSentence.pop()
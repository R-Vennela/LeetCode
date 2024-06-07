class Solution(object):
    def replaceWords(self, dictionary, sentence):
        wordlst = sentence.split(" ")
        dictionary = sorted(dictionary, key=len)
        for i in range(len(wordlst)):
            for r in dictionary:
                if wordlst[i][0:len(r)] == r:
                    wordlst[i] = r
                    break
        return " ".join(wordlst)
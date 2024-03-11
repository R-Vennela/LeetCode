class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged_string = ""
        word_len = min(len(word1),len(word2))
        for i in range(word_len):
            merged_string+= word1[i]
            merged_string+= word2[i]
        
        merged_string+= word1[word_len::]
        merged_string+= word2[word_len::]
        return merged_string 
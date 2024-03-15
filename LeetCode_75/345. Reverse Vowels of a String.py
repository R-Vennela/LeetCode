class Solution:
    def reverseVowels(self, s) :
        s = list(s) # convert string to list
        vowels = set("aeiouAEIOU")
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] not in vowels:
                low += 1
            elif s[high] not in vowels:
                high -= 1
            else:
                s[low], s[high] = s[high], s[low] # swap the chars
                low += 1
                high -= 1
        return "".join(s) # convert list to string  
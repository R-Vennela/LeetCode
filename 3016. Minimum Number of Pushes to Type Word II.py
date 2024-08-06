class Solution:
    def minimumPushes(self, word) :
        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))
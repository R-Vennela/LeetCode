class Solution:
    def timeRequiredToBuy(self, v, k) :
        n = len(v)
        t = 0
        while True:
            for i in range(n):
                if v[i] > 0:
                    v[i] -= 1
                    t += 1
                if i == k and v[i] == 0:
                    return t      
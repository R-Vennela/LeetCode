class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # Initialize a DP table with two rows
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
        
        prev[0] = True  # Empty pattern matches empty string

        # Fill the first row for patterns starting with *
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        # Fill the DP table
        for i in range(1, m + 1):
            curr[0] = False  # Reset the first column for each row
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = False
            prev, curr = curr, prev  # Swap rows

        return prev[n]
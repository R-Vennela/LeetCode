class Solution:
    def maxDepth(self, s) :
        # Initializing variables to keep track of depth and count of open parentheses.
        depth = 0  # Represents the maximum depth of nested parentheses encountered.
        count = 0  # Keeps track of the number of open parentheses encountered.

        # Iterating through each character in the string.
        for ch in s:
            # If the character is an open parenthesis '(',
            # increment the count of open parentheses encountered.
            if ch == '(':
                count += 1
                # Update the depth with the maximum of the current depth and the count of open parentheses.
                depth = max(depth, count)

            # If the character is a closing parenthesis ')',
            # decrement the count of open parentheses encountered.
            if ch == ')':
                count -= 1

        # Return the maximum depth found.
        return depth
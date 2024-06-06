from itertools import combinations
class Solution(object):
    def letterCombinations(self, digits):
        phone = {
          '2': ['a', 'b', 'c'],
          '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']
          }
        
        if not digits:
            return []
        elif len(digits) == 1:
            return phone[digits]
        else:
            results = phone[digits[0]]
            for digit in digits[1:]:
                results = [old + new for old in results for new in phone[digit]]
        return results
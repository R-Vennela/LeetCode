#Brute Force
class Solution:
    def rangeSum(self, nums, n, left, right):
        arr = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                arr.append(s)
        arr.sort()
        mod = 10**9 + 7
        return sum(arr[left - 1 : right]) % mod
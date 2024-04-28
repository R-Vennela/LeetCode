class Solution:
    def maxScore(self, nums, muls, k) :
        total_score = max_score = 0
        heap = []

        for mul, num in sorted(zip(muls, nums), reverse=True):
            heappush(heap, num)

            # Enlarge the window
            total_score += num

            # Reduce the window
            if len(heap) > k:
                total_score -= heappop(heap)

            # The current answer will be equal to the sum of the window multiplied by the current number,
            # since due to sorting it is now the smallest from all taken
            if len(heap) == k:
                max_score = max(max_score, total_score * mul)

        return max_score
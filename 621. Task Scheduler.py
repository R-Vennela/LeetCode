class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()
        print(freq)
        maxFreq = freq[25] - 1

        idleSlots = maxFreq * n
 
        for i in range(24, -1, -1):
            if freq[i] > 0:

                idleSlots -= min(maxFreq, freq[i])

        return idleSlots + len(tasks) if idleSlots > 0 else len(tasks)
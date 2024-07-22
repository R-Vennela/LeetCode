class Solution:
    def sortPeople(self, names, heights) :
        n = len(names)
        mapping = {}  # height -> name (heights are distinct)
        for ind in range(n):
            mapping[heights[ind]] = names[ind]

        heights.sort(reverse=True)
        for ind in range(n):
            h = heights[ind]
            names[ind] = mapping[h]

        return names
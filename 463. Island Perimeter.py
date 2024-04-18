
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tot = 0
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == 1:
                    tot += 4
                    if cell != 0 and grid[row][cell-1] == 1:
                        tot -= 2
                    if row != 0 and grid[row-1][cell] == 1 :
                        tot -= 2
        return tot
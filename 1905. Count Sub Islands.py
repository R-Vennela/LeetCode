class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """

        def bfs(currentN, currentM, n, m):
            top = not(currentN  <= 0)
            right = not(currentM == m -1)
            bottom = not(currentN == n -1)
            left = not(currentM <= 0)

            top_res = right_res = bottom_res = left_res = True

            grid2[currentN][currentM] = 0
            
            if top and grid2[currentN - 1][currentM] == 1:
                top_res = bfs(currentN - 1, currentM, n, m)

            if right and grid2[currentN][currentM + 1] == 1:
                right_res = bfs(currentN, currentM + 1, n, m)

            if bottom and grid2[currentN + 1][currentM] == 1:
                bottom_res = bfs(currentN + 1, currentM, n, m)

            if left and grid2[currentN][currentM - 1] == 1:
                left_res = bfs(currentN, currentM - 1, n, m)


            if grid1[currentN][currentM] == 0:
                return False

            return top_res and right_res and bottom_res and left_res

        n = len(grid1)
        m = len(grid1[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    if bfs(i,j,n,m):
                        count = count + 1
        return count
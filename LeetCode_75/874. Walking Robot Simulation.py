class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # east, south, west, north
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        idx, x, y, res = 3, 0, 0, 0
        
        for e in commands:
            if e == -2:
                idx = (3 + idx) % 4
            elif e == -1:
                idx = (1 + idx) % 4
            else:
                dx, dy = dirs[idx]
                for _ in range(e):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    res = max(res, x * x + y * y)
        
        return res
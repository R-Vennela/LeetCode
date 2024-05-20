class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0:
            return 0 

        points = sorted(points, key=lambda x:x[1])
        arrowLastHit = -float('inf')

        arrow = 0
        for point in points:
            if point[0] > arrowLastHit:
                arrow += 1
                arrowLastHit = point[1]
        return arrow
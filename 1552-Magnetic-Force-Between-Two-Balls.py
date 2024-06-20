class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n = len(position)
        
        def countBalls(distance):
            count = 1
            last_pos = position[0]
            for i in range(1, n):
                if position[i] - last_pos >= distance:
                    count += 1
                    last_pos = position[i]
            return count
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if countBalls(mid) >= m:
                left = mid
            else:
                right = mid - 1
        
        return left
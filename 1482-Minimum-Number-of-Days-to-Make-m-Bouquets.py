class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1
        
        def can_make_bouquets(day):
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left
        
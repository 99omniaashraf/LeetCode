class Solution(object):
    def isPerfectSquare(self, num):
        \\\
        :type num: int
        :rtype: bool
        \\\
        if num < 1:
            return False
        
        left, right = 1, num
        
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            
            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        
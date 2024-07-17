class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize a result list of the same size as nums
        n = len(nums)
        result = [0] * n
        
        # Two pointers approach
        left, right = 0, n - 1
        index = n - 1  # Start filling result from the end
        
        # Traverse from the end towards the start
        while index >= 0:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        
        return result
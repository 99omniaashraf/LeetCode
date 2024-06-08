class Solution(object):
    def checkSubarraySum(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: bool
        \\\
        remainder_map = {0: -1}
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False
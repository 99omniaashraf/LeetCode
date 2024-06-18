class Solution(object):
    def minPatches(self, nums, n):
        \\\
        :type nums: List[int]
        :type n: int
        :rtype: int
        \\\
        miss = 1
        index = 0
        patches = 0
        
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                patches += 1
        
        return patches
        
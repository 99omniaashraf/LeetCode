class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        remainders = {0: 1}  # Initialize with 0 remainder

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:  # Handle negative remainders
                remainder += k
            if remainder in remainders:
                count += remainders[remainder]
            remainders[remainder] = remainders.get(remainder, 0) + 1

        return count
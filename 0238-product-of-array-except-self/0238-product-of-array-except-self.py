class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        # Pass 1: Left products
        left_prod = 1
        for i in range(len(nums)):
            res[i] = left_prod
            left_prod *= nums[i]
            
        # Pass 2: Right products
        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
            
        return res
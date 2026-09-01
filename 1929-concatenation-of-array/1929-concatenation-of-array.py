class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        j=0
        for j in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans


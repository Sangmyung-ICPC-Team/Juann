class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for idx in range(1, n):
            nums[idx] = max(nums[idx-1]+nums[idx], nums[idx])
        return max(nums)

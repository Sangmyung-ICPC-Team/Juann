class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        nums.remove(m)
        n = max(nums)
        
        return (m - 1) * (n - 1)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashTable = {}
        for value in nums:
            if value not in hashTable:
                hashTable[value] = True
            else:
                return True

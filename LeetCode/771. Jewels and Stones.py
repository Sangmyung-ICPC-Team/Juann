class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelsLen = len(jewels)
        stonesLen = len(stones)
        
        count = 0
        for word in stones:
            for j in jewels:
                if word == j:
                    count += 1
        return count

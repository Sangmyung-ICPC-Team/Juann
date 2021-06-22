#Runtime: 12ms / Memory: 13300KB
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = list()
        result.append([1])
        if numRows == 1:
            return result
        
        result.append([1, 1])

        
        for i in range(2, numRows):
            result.append([result[i-1][0]])
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(result[i-1][i-1])
            
        return result
      

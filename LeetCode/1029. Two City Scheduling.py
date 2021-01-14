def get_min_max(a, b):
        if a[0] >= a[1]:
            n1 = (a[0] - a[1])
        else:
            n1 = (a[1] - a[0])
        if b[0] >= b[1]:
            n2 = (b[0] - b[1])
        else:
            n2 = (b[1] - b[0])
        return n2 - n1
    
class Solution(object):
        
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        result = sorted(costs, cmp = get_min_max)
        
        sum = 0
        A = 0
        B = 0
        N = len(costs) / 2
        
        for i in range(len(costs)):
            if(A == N):
                for j in range(i, len(costs)):
                    sum = sum + result[j][1]
                break
            if(B == N):
                for j in range(i, len(costs)):
                    sum = sum + result[j][0]
                break
            if(result[i][0] <= result[i][1]):
                A = A + 1
                sum = sum + result[i][0]
                continue
            if(result[i][0] >= result[i][1]):
                B = B + 1
                sum = sum + result[i][1]
                continue
        return sum

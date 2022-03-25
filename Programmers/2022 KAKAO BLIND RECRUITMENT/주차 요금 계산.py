import math
def solution(fees, records):
    answer = []
    
    basicTime, basicFee, t, f = fees
    
    arr = {}
    
    # create dataset
    for element in records:
        x, y, z = element.split() # time, num, stat
        
        # init
        if y not in arr:
            arr[y] = []
        
        # insert
        if z == "IN":
            arr[y].append([x, 0])
        else: 
            arr[y].append([x, 1])

    # filter
    for key in arr:
        temp = arr[key].pop(-1)
        arr[key].append(temp)

        if temp[1] == 1: # out
            continue
        arr[key].append(["23:59", 1])
    
    
    for key in sorted(arr):
        total = 0
        for i in range(0, len(arr[key]) - 1, 2):
            a, b = arr[key][i+1][0].split(':')
            t1 = int(a)*60 + int(b)
            
            a, b = arr[key][i][0].split(':')
            t2 = int(a)*60 + int(b)
            
            total += t1 - t2 # 이용시간 계산
            
            
        if total <= basicTime:
            answer.append(basicFee)
        else:
            total -= basicTime
            answer.append(math.ceil(total/t)*f +basicFee)
    print(arr)
    return answer

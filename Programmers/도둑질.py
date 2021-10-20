def solution(money):
    
    m1 = money[:-1] #첫 집을 선택, 마지막 집 x
    m2 = money[1:] #첫 집 x, 마지막 집 선택
    
    dp1 = [0 for _ in range(len(money))] #m1 case
    dp2 = [0 for _ in range(len(money))] #m2 case
    
    #첫 번째 경우는 무조건 한 집만 갈 수 있다.
    dp1[1], dp2[1] = money[0], money[1] 
    #둘 째 경우는 첫번 째 집 or 두번 째 집 중 큰 곳만 갈 수 있다.
    dp1[2], dp2[2] = max(money[0], money[1]), max(money[1], money[2]) 
    
    for idx in range(3, len(money)):
        #curr_idx의 값은 idx-1 or idx-2 + each m의 idx-1 값이다.
        dp1[idx] = max(dp1[idx-1], m1[idx-1] + dp1[idx-2])
        dp2[idx] = max(dp2[idx-1], m2[idx-1] + dp2[idx-2])
    return max(dp1[len(m1)], dp2[len(m2)])

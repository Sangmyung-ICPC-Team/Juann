def solution(id_list, report, k):
    answer = []
    
    arr_1, arr_2 = {}, {}
    
    # init
    for user in id_list:
        arr_1[user] = []
        arr_2[user] = 0
    
    # insert 
    for message in report:
        user1, user2 = message.split()
        # only ones
        if user2 not in arr_1[user1]:
            arr_1[user1].append(user2)
            arr_2[user2] += 1
    
    # filter
    target = []
    for key in arr_2:
        if arr_2[key] >= k:
            target.append(key)
            
    for key in arr_1:
        temp = 0
        for t in target:
            if t in arr_1[key]:
                temp += 1
        answer.append(temp)
    
    
    return answer

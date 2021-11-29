def solution(record):
    #define
    answer = []
    manage = {}
    chat = []
    
    #exec
    for cmd in record:
        temp = cmd.split()
        if temp[0] == 'Enter':
            manage[temp[1]] = temp[2]
            chat.append([temp[0], temp[1]])
        elif temp[0] == 'Leave':
            chat.append([temp[0], temp[1]])
        elif temp[0] == 'Change':
            manage[temp[1]] = temp[2]
    
    #result
    for c in chat:
        if c[0] == 'Enter':
            cmd = manage[c[1]] + "님이 들어왔습니다."
            answer.append(cmd)
        elif c[0] == 'Leave':
            cmd = manage[c[1]] + "님이 나갔습니다."
            answer.append(cmd)
    
    return answer

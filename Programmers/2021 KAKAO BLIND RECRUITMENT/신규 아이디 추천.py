def to_lower(new_id): #1
    return new_id.lower()
 
def remove_word(new_id): #2
    poss = ['-', '_', '.']
    res = ""
    for word in new_id:
        if word in poss or word.isalpha() or word.isdigit():
            res += word
    return res

def detect_dot(new_id):
    flag = False
    res = ""
    for word in new_id:
        if word == '.':
            if flag: #전에 .이 나왔다면
                continue
            flag = True
        else:
            flag = False
        res += word
    return res

def is_dot(new_id): #4
    #빈 문자열인 경우 그대로 반환
    if len(new_id) <= 0:
        return new_id
    
    if new_id[0] == '.':
        new_id = new_id[1:]
        
    if len(new_id) <= 0:
        return new_id
    #
    if new_id[len(new_id) - 1] == '.':
        new_id = new_id[:len(new_id) - 1]

    return new_id

def is_empty(new_id): #5
    if len(new_id) <= 0:
        return 'a'
    return new_id

def split(new_id): #6
    if len(new_id) < 16: 
        return new_id
    
    new_id = new_id[:15]
    if new_id[len(new_id) - 1] == '.':
        new_id = new_id[:len(new_id) - 1]
    
    return new_id

def is_short(new_id): #7
    while len(new_id) <= 2:
        new_id += new_id[len(new_id) - 1]
    
    return new_id

def solution(new_id):
    return is_short(split(is_empty(is_dot(detect_dot(remove_word(to_lower(new_id)))))))

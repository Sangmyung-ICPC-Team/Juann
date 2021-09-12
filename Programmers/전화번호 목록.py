def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    phoneDict = {}
    for num in phone_book:
        temp = ""
        for w in num:
            temp += w
            if temp in phoneDict:
                return False
        phoneDict[num] = True
    
    return answer

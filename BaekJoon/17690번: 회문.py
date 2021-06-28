def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

def check_palindrome(word, p1, p2):
    while p1 < p2:
        if word[p1] != word[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

def is_pseudo(word): #not same at least one word
    length = len(word)
    p1, p2 = 0, length-1
    while p1 < p2:
        if word[p1] != word[p2]:
            #p1 + 1
            if check_palindrome(word, p1 + 1, p2) or check_palindrome(word, p1, p2 - 1):
                return True
            else:
                return False
        p1 += 1
        p2 -= 1

T = int(input())

for _ in range(T):
    word = input()
    if is_palindrome(word):
        print(0)
    else:
        if is_pseudo(word):
            print(1)
        else:
            print(2)

def balance(n, arr, idx):
    newStr = ""
    for _ in range(n - len(arr[idx])):
        newStr += '0'
    return newStr


def solution(n, arr1, arr2):
    ans = []
        
    for idx, value in enumerate(arr1):
        arr1[idx] = format(value, 'b')
        if len(arr1[idx]) < n:
            arr1[idx] = (balance(n ,arr1, idx) + arr1[idx]) #append
            
    for idx, value in enumerate(arr2):
        arr2[idx] = format(value, 'b')
        if len(arr2[idx]) < n:
            arr2[idx] = balance(n ,arr2, idx) + arr2[idx] #append

    
    for a1, a2 in zip(arr1, arr2):
        newStr = ""
        for idx in range(len(a1)):
            if a1[idx] == '1' or a2[idx] == '1':
                newStr += '#'
            else:
                newStr += ' '
        ans.append(newStr)
    
    return ans

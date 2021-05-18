from collections import deque

num = int(input())

dic = {} #alpha set
array = deque()
size = []

for i in range(num):
    array.append(list(input()))
    size.append(len(array[i]))


#sort by length
array.sort(key=lambda x:len(array))
size.sort()


#number set 0 ~ 9
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#input alpha set
while len(size):
    

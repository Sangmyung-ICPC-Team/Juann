def solution(genres, plays):
    answer = []
    
    dictionary = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dictionary:
            dictionary[genre] = [0]
        dictionary[genre].append([play, idx])
        dictionary[genre][0] += play

        
    temp = sorted(dictionary.items(), key=lambda x: x[1][0], reverse=True)
    print(temp)
    for values in temp:
        values[1].pop(0) #버림 
        values[1].sort(key=lambda x: x[0], reverse=True)
        print(temp)
        cnt = 0
        while len(values[1]) > 0:
            if cnt == 2:
                break
            answer.append(values[1][0][1])
            values[1].pop(0)
            cnt += 1
    
    return answer

'''
Accepted Solutions Runtime Distribution = 99.49%
'''
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        gh = {}  
        # enumerate는 index까지 반환한다
        for idx, word in enumerate(words): # 0, bella / 1, label / 2, roller
            for w in word: # b e l l a
                if w not in gh:
                    gh[w] = [0 for _ in range(len(words))]
                gh[w][idx] += 1 # 개수 1 증가
        
        answer = []
        for key in gh:
            temp = min(gh[key]) # 가장 작은 값을 search
            if temp < 1: # 한 번이라도 안 나왔으면 
                continue # 건너뛰기
            for res in range(temp): # 한 번이라도 나왔으면
                answer.append(key) # 나온 갯수만큼 결과에 추가
            
        return answer

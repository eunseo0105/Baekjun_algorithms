import math

def solution(progresses, speeds):
    value = [] 
    count = 1
    for i in range(len(progresses)):
        ans = math.ceil((100- progresses[i])/speeds[i])
        value.append(ans)
    
    now = 0
    answer = []
    for i in range(1,len(value)):
        if value[i] > value[now]:
            answer.append(i - now)
            now = i
    answer.append(len(value) -now)
    
      
    
    
            
    return answer

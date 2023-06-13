def solution(array, commands):
    answer = []
    result = 0 
    for value in commands:
        i = value[0]
        j = value[1]
        k = value[2]
        l = i-1
        array2= sorted(array[l:j])
        print(sorted(array[l:j]))
        result = array2[k-1]
        answer.append(result)
        
    return answer
        
        

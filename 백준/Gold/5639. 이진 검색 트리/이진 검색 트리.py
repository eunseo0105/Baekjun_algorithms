import sys
sys.setrecursionlimit(10 ** 9)

# 변수 초기화
node = []

while True:
    try:
        temp = int(input())
    except:
        break
    node.append(temp)

def divide(node, start, end):
    #들어온 값이 없는 경우
    if end == start:
        return []
    #값이 하나 들어온 경우
    if end-start <= 1:
        return [node[start]]

    #루트 노드는 전위순회에서 맨 처음 
    root = node[start]
    
    find_idx = end
    for i in range(start+1, end):
        if node[i] > root:
            find_idx = i
            break
    tree = divide(node, start+1, find_idx) + divide(node, find_idx, end) + [node[start]] # 왼+오+루트
    return tree

tree = divide(node, 0, len(node))
for t in tree:
    print(t)
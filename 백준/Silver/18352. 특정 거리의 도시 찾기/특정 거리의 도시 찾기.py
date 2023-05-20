import sys
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [-1]*(N + 1)
visited[X] = 0

for i in range(M):
    o, t = map(int, sys.stdin.readline().split())
    graph[o].append(t)

queue = deque()
queue.append(X)

while queue:
    now = queue.popleft()

    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            queue.append(i)

check = False
for i in range(1, N + 1):
    if visited[i] == K:
        print(i)
        check = True

if not check:
    print(-1)
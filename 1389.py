# 1389 - 케빈 베이컨의 6단계 법칙
# 플로이드 워셜 알고리즘
# solved

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Graph = [[5000*100 for _ in range(N)] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    Graph[a-1][b-1] = 1
    Graph[b-1][a-1] = 1

for n in range(N):
    Graph[n][n]=0
    
for n in range(N):
    for a in range(N):
        for b in range(N):
            s = min(Graph[a][b], Graph[n][a]+Graph[n][b])
            Graph[a][b] = s

minidx = 0
t = 5000*100
for i in range(N):
    if sum(Graph[i]) < t:
        minidx = i
        t = sum(Graph[i])  
print(minidx+1)
    
# 7569 - 토마토
# BFS
# solved

import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
Box = [[] for level in range(H)]
Queue = deque([])

for z in range(H):
    for y in range(N):
        Box[z].append(list(map(int, input().split())))
        for x in range(M):
            if Box[z][y][x]==1:
                Queue.append((x,y,z))

while Queue:
    x,y,z = Queue.popleft()
    
    for p in [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]:
            if 0<=p[0]<M and 0<=p[1]<N and 0<=p[2]<H:
                if Box[p[2]][p[1]][p[0]]==0:
                    Queue.append(p)
                    Box[p[2]][p[1]][p[0]] = Box[z][y][x]+1


max=0
for z in range(H):
    for y in range(N):
        for x in range(M):       
            if Box[z][y][x]==0:
                print(-1)
                exit(0)
            elif Box[z][y][x]>max:
                max=Box[z][y][x]
print(max-1)
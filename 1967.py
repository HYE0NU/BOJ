# 1967 - 트리의 지름
# DFS
# solved

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
Map = [[] for _ in range(n)]

for i in range(n-1):
    p, q, d = map(int, input().split())
    Map[p-1].append((q-1, d))
    Map[q-1].append((p-1, d))

def dfs(start, Map):
    dist = [-1 for _ in range(n)]
    dist[start] = 0
    maxnode = start
    
    stack = deque([])
    deque.append(stack, start)
    
    while stack:
        parent = deque.pop(stack)
        for l in Map[parent]:
            if dist[l[0]] == -1:
                deque.append(stack, l[0])
                dist[l[0]] = dist[parent] + l[1]
                
                if dist[l[0]] > dist[maxnode]:
                    maxnode = l[0]
            
    return maxnode, dist[maxnode]

p1, dist = dfs(0, Map)
p2, dist = dfs(p1, Map)

print(dist)
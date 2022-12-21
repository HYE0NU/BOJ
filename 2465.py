# 2465 - 줄 세우기
# solved

import sys
input = sys.stdin.readline

N = int(input())
Height = []
S = []

for n in range(N):
    Height.append(int(input()))
    
S = list(map(int, input().split()))

Height.sort()
Line = [0 for _ in range(N)]

for i in range(N-1,-1,-1):
    Line[i] = Height.pop(S[i])
    
for i in range(N):
    print(Line[i])
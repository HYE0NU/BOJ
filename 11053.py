# 11053 - 가장 긴 증가하는 부분 수열
# DP
# solved

import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))

maxlen=[1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if l[i]>l[j]:
            maxlen[i] = max(maxlen[i], maxlen[j]+1)           

print(max(maxlen))
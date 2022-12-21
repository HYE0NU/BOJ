# 1107 - 리모컨
# brute force
# solved

import sys
input = sys.stdin.readline

nums = [True for _ in range(12)]
dest = int(input())
M = int(input())
channel = 100

if M>0:
    L = list(map(int, input().split()))

    for m in L:
        nums[m] = False
    
mincnt = abs(dest-channel)

for p in range(max(200, 2*dest)):
    cnt = 0
    vailable = True
    
    for c in str(p):
        if not nums[int(c)]:
            vailable = False
    if not vailable:
        continue
    
    cnt = len(str(p)) + abs(dest-p)
        
    if cnt<mincnt:
        mincnt = cnt
        
print(mincnt)
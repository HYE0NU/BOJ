# 11286 - 절댓값 힙
# heap
# solved

import sys
input = sys.stdin.readline
from heapq import *

N = int(input())
H = []

for n in range(N):
    x = int(input())
    
    if x==0:
        if H:
            print(heappop(H)[1])
        else:
            print(0)
    else:
        heappush(H, (abs(x), x))
# 1708 - 볼록 껍질
# Monotone Algorithm
# Solved

import sys
input = sys.stdin.readline    

def CCW(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1]-p1[1]) # p2-p1
    v2 = (p3[0]-p1[0], p3[1]-p1[1]) # p3-p1
    
    return v1[0]*v2[1]-v1[1]*v2[0]  # v1 x v2

            
N = int(input())
P = []
count = 0

for n in range(N):
    x, y = map(int, input().split())
    P.append((x,y))

P.sort()

Lower = []
for p in P:
    while len(Lower) >= 2 and CCW(Lower[-2], Lower[-1], p) <= 0:
        Lower.pop()
    Lower.append(p)
    
Upper = []
for p in reversed(P):
    while len(Upper) >= 2 and CCW(Upper[-2], Upper[-1], p) <= 0:
        Upper.pop()
    Upper.append(p)
    
ConvexHull = Lower[:-1]+Upper[:-1]

print(len(ConvexHull))
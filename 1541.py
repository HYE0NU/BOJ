# 1541 - 잃어버린 괄호
# greedy

import sys
input = sys.stdin.readline

L = input().strip()

num = 0
ischar = False
isnum = False

for c in L:
    if c
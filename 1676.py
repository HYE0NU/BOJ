# 1676 - 팩토리얼 0의 개수
# math
# solved

import sys
input = sys.stdin.readline

N = int(input())

cnt = 0

cnt += N//5
cnt += N//25
cnt += N//125

print(cnt)

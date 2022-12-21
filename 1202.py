# 1202 - 보석 도둑
# solved

import sys
input = sys.stdin.readline

import heapq

N, K = map(int, input().split())
Jewels = []
AbleJewels = []
Bags = []
sum = 0

# input
for n in range(N):
    mass, value = map(int, input().split())
    heapq.heappush(Jewels, (mass, value)) # minheap
    
for k in range(K):
    capacity = int(input())
    Bags.append(capacity)
Bags.sort()

# heap 
for bag in Bags:
    while Jewels and Jewels[0][0]<=bag:
        heapq.heappush(AbleJewels, -heapq.heappop(Jewels)[1]) # maxheap

    if AbleJewels:
        sum += -heapq.heappop(AbleJewels)
            
print(sum)
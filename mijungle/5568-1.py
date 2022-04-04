import sys
from itertools import permutations

input = sys.stdin.readline

n,k = int(input()), int(input())

m = [ input().rstrip() for _ in range(n)]

ans = set()

for per in permutations(m, k):
    ans.add(''.join(per))

print(len(ans))

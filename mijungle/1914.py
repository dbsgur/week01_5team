import sys
from itertools import permutations

x, y = int(input()), int(input())
m = [input().rstrip() for _ in range(x)]

ans = set()
for per in permutations(m, y):
    ans.add(''.join(per))
    
print(ans)
print(len(ans))
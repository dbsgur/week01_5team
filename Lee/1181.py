import sys

input=sys.stdin.readline

n= int(input())

li=[]
for i in range(n):
    word=input().strip()
    li.append(word)

total = set(sorted(li))
print(total)
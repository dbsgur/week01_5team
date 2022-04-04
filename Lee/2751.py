import sys

input= sys.stdin.readline

n=int(input())

li=[]
for i in range(n):
    num = int(input())
    li.append(num)

for i in sorted(li):
    print(i)
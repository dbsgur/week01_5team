# import sys

# input = sys.stdin.readline #변수로 지정해서 쓰기 이거 쓸 때는 sys import해서 적어야합니다.

# total = []

# for i in range(9):
#     total.append(int(input()))


a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
f= int(input())
g= int(input())
h= int(input())
i= int(input()) #ㅋㅋㅋㅋㅋㅋㅋ 하나씩 다 받고

total = [a,b,c,d,e,f,g,h,i] #리스트로 생성하고

print(max(total)) #리스트 내에서 최대값 찾고
print((total.index(max(total))+1)) #최대값이 그 리스트의 몇번째 인덱스인지, 그리고 거기에 +1을 해서 보통처럼
import sys
import math

input=sys.stdin.readline

# n=int(input())

# print(math.factorial(n)) #math 라이브러리에 factorial 함수를 사용하면 된다.

# index=[]
# for i in range(1,n+1): #1~10까지
#     index.append(i) #[1,2,...,10]

# # print(index[0]) #1이 나오고 있어

# # print(index[i]*index[i])

# while n<n+1:
#     index[]

n=int(input())

def fac(n):
    if n>0:
        # result = 0
        # result= n*fac(n-1)
        return n * fac(n-1)
    else:
        return 1

print(fac(n))
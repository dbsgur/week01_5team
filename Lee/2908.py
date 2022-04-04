import sys

input=sys.stdin.readline

a,b=input().split() #str

# print(a[::-1])

# if int(a)>int(b):
#     print(a[::-1])
# else:
#     print(b[::-1])

a=a[::-1] #[::-1]이 문자를 거꾸로 써줌 734 > 437로
b=b[::-1]

if a>b: #뒤집은 a가 b보다 크면
    print(a)
else:
    print(b)
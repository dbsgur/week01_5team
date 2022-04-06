import sys

input=sys.stdin.readline

a,b=input().split() #str

a=a[::-1] #[::-1]이 문자를 거꾸로 써줌 734 > 437로
b=b[::-1]

if a>b:
    print(a)
else:
    print(b)
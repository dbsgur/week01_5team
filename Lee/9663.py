import sys

input=sys.stdin.readline

n=int(input())

# i열에 있는 퀸의 행의 값은 row[i]
# 처음 if 문은 무한루프를 탈출하기 위한 기능이고 
# 한정 함수의 조건을 만족하면 재귀함수로 들어가게..
# 재귀함수는 다음 열로 계속 진행시켜 주는 것이고 
# n범위까지의 for문은 행을 다음 행으로 계속 진행시켜 주는 것
# abs()는 절대값을 구하는 함수입니다.

row = [0]*n #list n개 생성

def check(x):
    for i in range(x):
        if row[i]==row[x] or abs(row[x]-row[i]) == x-i:
            return False
    return True

result=0
def queen(x):
    global result #전역으로 지정 안 해주면 안 돌아가

    if x==n: 
        result+=1 #카운트
    else:
        for i in range(n): #x(0)~8까지
            row[x]=i
            if check(x):
                queen(x+1)

queen(0) #0부터 시작
print(result)
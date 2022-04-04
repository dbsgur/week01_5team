import sys

input=sys.stdin.readline

#재귀재귀재귀재귀~함수
#3개의 기둥은 고정이 되어있습니다~ 1+2+3=6

n=int(input())

def cnt(start,end):
    print(start,end)

def hanoi(one,start,end):
    if one == 1:
        return cnt(start,end) #print
    pillar = 6-start-end
    hanoi(one-1,start,pillar)
    cnt(start,end) #print를 함수로 처리했으니까
    hanoi(one-1,pillar,end)

sum=0
for ni in range(n):
    sum=sum*2+1

#출력초과인 이유
if n>20: #20보다 크면 
    print(sum) #밑에 출력 안되게
else: #작으면 과정도 출력되게
    print(sum)
    hanoi(n,1,3)
import sys

input=sys.stdin.readline

# 탐색. 재귀
# n개 만큼 이루어진 수열
# 연산자 개수 입력 + - * / 총 4개 >> if cal[0] > 0: num[0:1] elif cal[1] >0: -해주고.. 이런
# 주어진 수 순서 바꿈x
# 연산자 우선 순위 무시하고, 나눗셈은 몫만 가능 ex. 1/2 = 0.5인데 .5없애고 '0만 받습니다'
# math.trunc = 소수점 버림 하는 방법 // "그냥 int 붙여주면 됩니다"
# 음수/양수는 일단 양수로 받고 음수를 붙여주는걸로ㅇㅇ~
# 만든 식 중 최대인 식의 결과와 최소인 식의 결과만 개행으로 출력

n=int(input())
num = list(map(int, input().split())) #[5, 6]
cal = list(map(int, input().split())) # [0, 0, 1, 0]

maxim = -1e9 #1,000,000,000
minim = 1e9

def dfsBack(exp,total,plus,minus,mul,divi):
    global maxim, minim #전역변수로
    if exp == n:
        maxim = max(total,maxim)
        minim = min(total,minim)
        return

#순서대로 +,-,*,/에 있을시 돌리고 횟수 -1해줌 == 그러면 0횟수로 안 돌게 해주는거지
# 반대로 exp엔 +1을 해줌으로 돌린 횟수를 추가해서 위에 exp ==n횟수와 같으면 종료되게
    if plus:
        dfsBack(exp+1,total+num[exp],plus-1,minus,mul,divi)
    if minus:
        dfsBack(exp+1,total-num[exp],plus,minus-1,mul,divi)
    if mul:
        dfsBack(exp+1,total*num[exp],plus,minus,mul-1,divi)
    if divi:
        dfsBack(exp+1,int(total/num[exp]),plus,minus,mul,divi-1)

dfsBack(1,num[0],cal[0],cal[1],cal[2],cal[3])
# total은 num[0]부터 사칙 시작하니까! cal[0]부터 차례대로 + - * /임

print(maxim)
print(minim)


# def plus():
#     if cal[0]>0:
#         return num[i]+num[i+1]

# def minus():
#     if cal[1]>0:
#         return num[i]-num[i+1]

# def mul():
#     if cal[2]>0:
#         return num[i]*num[i+1]

# def divi():
#     if cal[3]>0:
#         return -abs(num[i]/num[i+1]) # 맞나?ㅋㅋ

# for i in num:
#     print(i)

# cal()
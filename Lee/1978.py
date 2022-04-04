import sys

input=sys.stdin.readline

n=int(input())
nums=map(int, input().split()) #숫자들은 int로 잘 담겨있지만, 프린트는 <map object at 0x00605CB0>로 뜸
#이유가 >> 필요할 때만 하나씩 꺼내보여주기 때문이래

so = 0 #소수일 때 카운팅 담을 변수
for num in nums: # 3 \n 4 하니씩
    x=0 # 소수 아닐 때 카운팅
    if num>1: #만약 num의 수가 1보다 크면 [왜냐면 1은 소수가 아님!]
        for i in range(2,num): #2부터 n범위까지 돌리는 i
            if num % i == 0: #num과 i에 나머지가 0이면 소수가 아님!
                x+=1 #소수가 아닐시 카운트 올림
        if x == 0: #위에 반복문이 끝났을 때 x가 카운트가 0이면
            so+=1  #소수에 카운팅해줌

print(so)
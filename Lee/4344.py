import sys

input = sys.stdin.readline

c=int(input())

for ci in range(c): #c범위만큼 돌고
    a = list(map(int, input().strip().split()))
    # print(a[0]) #학생수
    # print(sum(a[1:])) #함수 sum을 사용하면 리스트 요소 값끼리 합 해줍니다.
    avr = sum(a[1:])/a[0] #학생수만큼의 평균점수
    # print(round(avr,3)) #round(실수, n) == n자리 소수까지 반올림하는 함수//근데 여기선 사용불가
    count = 0
    for score in a[1:]: #하나씩 배출(?)
        if score>avr:
            count+=1 #avr을 넘는 점수를 가진 애만 카운트가 되게
    rate = count/a[0]*100 #점수가 100이 만점이니까 100으로(?) 이거 맞나용
    print(f'{rate:.3f}%') #f-string이라는 건데 f'{변수:.xf}' 형식으로. 이때 x=소수몇짜리

    #이거 안 먹혔던 이유는 내가 %를 안 써서 그런거였음.. 맞았따~



# import sys

# input = sys.stdin.readline

# c=int(input())

# for ci in range(c):
#     a = list(map(int, input().strip().split()))
#     avr = sum(a[1:])/a[0]
#     count = 0
#     for score in a[1:]:
#         if score>avr:
#             count+=1
#     rate = count/a[0]*100
#     print(f'{rate:.3f}', end='')
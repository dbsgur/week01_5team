import sys

input=sys.stdin.readline

a=int(input())
b=int(input())
c=int(input())

# print(a*b*c) #17037300 정수임
result=list(str(a*b*c))
# print(result) #['1', '7', '0', '3', '7', '3', '0', '0']

for i in range(10): #0부터9까지의 숫자가 쓰였는지 // i는 지금 정수임 count는 문자를 세주는 함수
    print(result.count(str(i))) #i를 문자열로 바꿔서 result에서 세주는거 ex. i='0'일때 result '0'을 세주는거
    # result.count(i)
    # print(result)


# for i in [a*b*c]:
#     i.count
    # n=list(map(int,str(i))) #i를 문자열로 하고 다시 정수형으로 바꾸면서 리스트 안에 넣어준 것
    # print(n) #[1, 7, 0, 3, 7, 3, 0, 0]
    
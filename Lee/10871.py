n,x = list(map(int, input().split())) #list의 문자열을 int 형태로 변환해줌 10 5

a = list(map(int, input().split())) #밑에다가 써야지 따로 입력받을 수 있어서 n,x랑 문법 같아도 a는 따로 적어줌

for i in range(n): #n 범위만큼 i번 돌리게
    if a[i]<x:
        print(a[i])

# for i in a: #list a의 i
#     if i<x :
#        print(i, end=' ') # 띄어쓰기로 출력할 때 이렇게 end 붙여줘야 함
# def cal(a,b):
#     if 1<=a & b<=10000:
#         sum = a+b
#         min = a-b
#         mul = a*b
#         mok = a/b
#         mod = a%b
#     return sum,min,mul,int(mok),mod

# a=input()
# b=input()
# print(cal(a,b))

# print("HELOO")77


a,b = input().split() # a,b를 input으로 받는데 split()을 통해 공백을 기준으로 분리
a = int(a) #input 받을때 str이라서 int로 변환해줌
b = int(b)

print(a+b,a-b,a*b,int(a/b),a%b, sep='\n') #이건 제출 이후 바꾼거 sep='\n' 줄바꿔주는것

# 근데 난 자연수 조건도 안 썼고[이건 코테에서 신경안써도됨..], 출력이 첫번째 두번째 안 되었는데? 왜 성공
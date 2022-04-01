n = int(input())

i=0

for i in range (1,10): #i는 1~9까지
    mul = n*i #입력받은 n 곱하기 i범위
    print(n,'*',i,'=',mul) #반복문 안에 적어야지 프린트가 쫙 뽑힘

print(sep='\n') #개행
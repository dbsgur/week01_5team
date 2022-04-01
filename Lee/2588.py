#처음에 런타임 오류

a=int(input()) #처음에 split으로 내가 input을 받아서 값이 다 제대로 들어갔어도 valueError가 뜸..
b=input()

a= int(a) #472
b= list(b) # [3, 8, 5]

totalB = int(''.join(b)) #385

b3= int(b[0])
b8 = int(b[1])
b5 = int(b[2])

print(a*b5,a*b8,a*b3,a*totalB, sep='\n')
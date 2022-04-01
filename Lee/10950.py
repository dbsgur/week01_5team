t=int(input()) #숫자 받고

num= [input().split() for i in range(t)] #t만큼 num에 input을 받음


for i in range(t):
    print(int(num[i][0])+int(num[i][1])) #t범위만큼 프린트 시켜주게 만들었음.

# add1 = int(num[0][0])+int(num[0][1])
# add2 = int(num[1][0])+int(num[1][1])
# add3 = int(num[2][0])+int(num[2][1])
# add4 = int(num[3][0])+int(num[3][1])
# add5 = int(num[4][0])+int(num[4][1])

# print(add1,add2,add3,add4,add5,sep='\n')
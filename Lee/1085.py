# x,y,w,h = list(input().split())

# for data in x,y,w,h:
#     result = min(data)

# print(result)


x,y,w,h = input().split() #여러개 받고

x=int(x)
y=int(y)
w=int(w)
h=int(h) # int형으로 바꿔주고

wx = w-x #x까지 x거리고 w까지는 x+(w-x)를 한 값이니까 아래도 같음
hy = h-y 

data = x,y,wx,hy #모아서

print(min(data)) #최소값 구하는 함수(?) min()사용

# if x>wx:
#     print(wx)
# else:
#     print(x)

# if y>hy:
#     print(hy)
# else:
#     print(y)


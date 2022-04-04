import sys

input=sys.stdin.readline

#첫줄엔 가로 세로 길이 자연수
#잘라야 할 점선 개수
# 가로는 = 0 세로는 =1 로 표기해서 몇 번에서 자를건지 표시
#max() 요소에서 가장 큰 값 반환

garo,sero=map(int,input().split())

x = [0, garo]
y = [0, sero]

zumsun = int(input())

for i in range(zumsun):
    piece=list(map(int, input().split())) #[0, 3]
    if piece[0] == 0: #가로를 자르면
        y.append(piece[1]) #세로가 늘어나요
    else:
        x.append(piece[1])

y.sort() #append 하면 뒤의 요소로 들어가는데, 그걸 오름차순으로 정렬해줌
x.sort() #[0, 4, 10] [0, 2, 3, 8]

# result=0 #이게 내가 제출한 식 27-31코드
# for xi in range(len(x)-1):
#     for yi in range(len(y)-1):
#         result=max(result, (x[xi+1]-x[xi])*(y[yi+1]-y[yi])) 
# print(result)

maxX=[] #담을 list를 안 만들어주면 'int' object is not iterable 에러가 뜸
maxY=[]
for xi in range(len(x)-1): #0~2
    maxX.append(x[xi+1]-x[xi]) #[4,6] 
for yi in range(len(y)-1):
    maxY.append(y[yi+1]-y[yi])

print(max(maxX)*max(maxY)) #각 인덱스에서 최대값끼리 곱하면 넓이 완성~ 예~
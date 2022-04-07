import sys

input= sys.stdin.readline

li=[]
for i in range(9): #난쟁이9명
    n=int(input())
    li.append(n)
    # [20, 7, 23, 19, 10, 15, 25, 8, 13]

# li.sort()

# sum = sum(li)
# for i in li: #값 뽑
#     sum+=i #140
#     if sum<=100:
#         print(i)

for i in range(9): #0~8
    for j in range(i+1,9): #1~9 / j값부터 돌려
        if sum(li)-(li[i]+li[j]) == 100: #140-(li[0]+li[1])
            #빈 공간에 초과된 값을 저장해둬
            temp = li[i] # 15
            temp2 = li[j] #25
#remove는 값으로 삭제하는 겁니다~ 15랑 25가 있는 값 삭제
li.remove(temp)
li.remove(temp2)
li.sort() #정렬 수행

for i in li: #값 출력
    print(i)
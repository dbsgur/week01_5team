import sys
import math #math 함수를 사용하기 위해 임포트 시켜줘야함

input=sys.stdin.readline

a,b,v=map(int,input().split()) #map() 쓰면 int 한 줄에 처리할 수 있음

# day =0
# height =0

# while height<v: #높이가 v보다 낮다면
#     day+=1 #day에 하루씩 넣어주고
#     height+=a #높이엔 a미터만큼 더해줌 [하루 올라감]
#     if height ==v: #만약 높이가 v랑 같다면 다 올라간 거니까 멈추고
#         break
#     height-=b #if뒤에 빼준건 높이가 같아져도 빼주면 안되니까

# print(day) #이게 안 되는 이유는 시간초과가 발생해서..

# 총거리(v)=하루이동거리(a-b)*day // v-b인 이유는 하루 총 이동거리에 b만큼이 증발되니까..? [미끌림 방지?]
day=(v-b)/(a-b) # 원래라면 (a-b)*day=(v-b) 잖아, day를 구하려면 이걸 뭐라해.. 암튼 식 옮기기
total = math.ceil(day) #ceil()은 소수를 올림해주면서 int형으로 만들어준다.

print(total)
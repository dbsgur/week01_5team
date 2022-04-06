import sys

input=sys.stdin.readline

n= int(input())

li=[]
for i in range(n):
    word=input().strip()
    li.append(word)

li = list(set(li)) #먼저 중복을 제거해줘야함
li.sort() #먼저 알파벳 순서대로 정렬해주고
li.sort(key=len) #sort(Key=)를 쓰면 key값을 기준으로 정렬해준다. len이면 길이 정렬 // 이거 출력은 그냥

for i in li:
    print(i)
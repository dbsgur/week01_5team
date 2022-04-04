import sys

input=sys.stdin.readline

n=int(input()) #범위

for i in range(n):
    # s=list(input().strip()) #str로 input ['3', ' ', 'a', 'b', 'c']
    # two = (int(s[0])*s[2])+(int(s[0])*s[3])+(int(s[0])*s[4])
    # # third = (int(s[0])*s[2])+(int(s[0])*s[3])+(int(s[0])*s[4])+(int(s[0])*s[5])
    # print(two)

    num,word=input().split() #str a가 1번째 b가 2번째자너.. 와.. 이걸 생각못하다니 ㅋ
    for share in word: # a\nb\nc
        print(int(num)*share, end='') #end를 써주면 붙습니다
    print() #아무것도 입력 안 해주면 줄바꿈이 된대
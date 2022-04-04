import sys

input=sys.stdin.readline

a=input().strip() #input 이렇게 할 때 \n이 같이 붙는 현상 때문에 아스키코드로 반환이 안된거였음ㅋ

print(ord(a)) #ord()를 쓰면 아스키코드값으로 반환해줍니다.
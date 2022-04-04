import sys

input = sys.stdin.readline

n = int(input()) #자연수n이 주어짐

#1<=?<=N 한수의 개수 출력
#등차수열 쉽게 ?= range()함수 = range(시작값,끝값+1,간격)
#1자리수, 2자리수들은 모두 한수가 된다. 세자리는 상통하지 않을 수 있기에 다 한수 XX

if n< 100: #100미만의 한수는 99개임
    hansu = n
else:
    hansu=99
    for i in range(100,n+1): #99까지는 한수니까 제외하고 돌려야함 100~!!
        nList = list(map(int, str(i))) #i는 현재 int / 숫자는 각각의 자릿수로 숫자를 분리할 수 없대
        # 그래서 다시 자릿수 분리해주고 숫자로 만들어준대 >> [1, 0, 1]
        if nList[0]-nList[1] == nList[1]-nList[2]:
            hansu+=1
print(hansu)
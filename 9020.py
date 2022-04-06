import sys
import math

input = sys.stdin.readline

n = 10000

arr =[True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1): #2부터 n의 제곱근까지 모든 수 확인 sqrt()가 제곱근 함수
    if arr[i] == True:
        #i가 소수라면 i를 제외한 모든 배수 지우기
        j=2
        while i*j <=n:
            arr[i*j]=False
            j+=1

for i in range(2,n+1):
    if arr[i]: #참인경우
        print(i,end=' ') #여까지가 에라토스테네스의 체 구현하는 식입니다.. 6~20코드
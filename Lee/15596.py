import sys

input=sys.stdin.readline

def solve(a): # ex. a = [1,2,3]
    ans=0
    for i in a: # 1 2 3
        ans+=i # ((0+1)+2)+3 -> ans에 담김
    return ans # ans 리턴


#sum() 함수는 [1,2,3] 같이 리스트 안의 숫자를 합해주는 함수 => 6

# n=int(input()) #정수값

# i=[]
# for a in range(n):
#     i.append(a)
# print(sum(i))
#----------------------------------ㅋㅋ^^
# def num(n):
#     i=[]
#     for a in range(n):
#         i.append(a)
#     return sum(i)

# print(num(int(input())))
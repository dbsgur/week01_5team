import sys

input=sys.stdin.readline

n=int(input())

makeList = []
for i in range(n):
    num = int(input()) #n번까지 입력받는 것
    makeList.append(num) #[5, 2, 3, 4, 1]

# for i in ma
#     pivot = makeList//2

for i in sorted(makeList):
    print(i)


# def quick(n):
#     if len(n)<=1:
#         return n #n범위가 1보다 작거나 같다면 그냥 n만 출력하게~

#     pivot = n[len(n)//2]
#     left,middle,right=[],[],[] #각각 list 생성해주고
    
#     for i in n:
#         if n<pivot:
#             left.append(i)
#         elif n>pivot:
#             right.append(i)
#         else:
#             middle.append(i)
#     return quick(left)+middle+quick(right)

# n=list(map(int, input().strip()))
# quick(n)
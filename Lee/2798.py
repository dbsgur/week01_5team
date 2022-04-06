import sys

input=sys.stdin.readline

n,m=map(int, input().split())
card = list(map(int, input().split())) #그냥 리스트로 받아버려~
#[5, 6, 7, 8, 9]

# l = len(card)
near = 0

for i in range(0,n-2): #0~
    for j in range(i+1,n-1): #1~
        for k in range(j+1,n): #2~ // k로 먼저 돌려
            if (card[i]+card[j]+card[k]>m):
                continue
            else:
                near=max(near,card[i]+card[j]+card[k]) 
                #5+6+7=18이 나왔을때 near에 담고 이후 k[3]으로 5+6+8=19 했을때 18,19중 최대인
                # 19값이 near에 담긴다~ 최대값은 max()함수

print(near)
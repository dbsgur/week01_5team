# 다시 풀기
import sys

input = sys.stdin.readline

y, x = map(int, input().split())

N = int(input())

x_list = [0, x]
y_list = [0, y]

for _ in range(N):
    xy, length = map(int, input().split())
    if xy == 0:
        x_list.append(length)
    else:
        y_list.append(length)

max_square = 0
x_list.sort()
y_list.sort()
# print(x_list)
# print(y_list)

for x_index in range(1, len(x_list)):
    for y_index in range(1, len(y_list)):
        width = x_list[x_index] - x_list[x_index-1]
        height = y_list[y_index] - y_list[y_index-1]
        max_square = max(max_square, height*width)

print(max_square)

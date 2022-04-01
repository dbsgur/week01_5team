import sys

input = sys.stdin.readline

num1 = int(input())
num2 = input()

result = 0
for i in range(3):
    mul = num1 * int(num2[2-i])
    print(mul)
    result += (mul * (10 ** i))

print(result)

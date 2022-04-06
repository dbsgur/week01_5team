
import sys

input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

# S = list(S)
# T = list(T)

lengthS = len(S)

result = []


def game(arr):
    if lengthS == len(arr):
        return arr == S
    if arr[0] == 'B' and game(arr[:0:-1]):
        return True
    if arr[-1] == 'A' and game(arr[:-1]):
        return True


print(1 if game(T) else 0)

button = False


def find(arr):
    global button
    if len(arr) == len(S):
        if arr == S:
            button = True
        return

    if arr[0] == 'B':
        arr = arr[::-1]
        arr.pop()
        find(arr)
        arr.append("B")
        arr = arr[::-1]
    if arr[-1] == 'A':
        arr.pop()
        find(arr)
        arr.append('A')


find(T)
print("###")
if button:
    print(1)
else:
    print(0)

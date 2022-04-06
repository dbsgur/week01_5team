import sys

input = sys.stdin.readline


N = int(input())

# coordinate = [[0]*(2**N)]*(2**N)
# 위 방법으로 배열을 선언하게 되면 얕은 복사가 일어난다.
# 단순히 요소를 복사하다 보니 바라보는 객체는 동일하다.
# 즉, 이러한 방식으로 선언한 뒤에, 값을 변경하게 되면 다른 원소들도 값이 변경되는
# 현상이 발생하게 되므로 이를 인지하고,
# 후에 대입연산자를 통해 값을 변경하지 않는 경우에만 사용하는 것이 좋다.

coordinate = [[0]*(2**N) for i in range(2**N)]
# print(coordinate)


def star(N, x, y):
    if N == 0:
        # print("*")
        coordinate[x][y] = "*"
        return
    else:
        gap = 2**(N-1)
        star(N-1, x, y)
        star(N-1, x, y+gap)
        star(N-1, x+gap, y)


star(N, 0, 0)

for x in range(2**N):
    for y in range(2**N-x):
        if coordinate[x][y] == "*":
            print("*", end='')
        else:
            print(" ", end='')
    print("")
# print(coordinate)

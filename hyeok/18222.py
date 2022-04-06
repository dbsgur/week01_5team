import sys

input = sys.stdin.readline

k = int(input())


def tooe_mose(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2:
        return 1 - tooe_mose(n//2)
    else:
        return tooe_mose(n//2)


print(tooe_mose(k-1))

# 메모리 초과
# # 시간복잡도 줄이기 카운트 추가 ?
# # count 몇번 반복했는지, value 값
# def ex(value):
#     print(f"value : {value}")
#     print(f"k : {k}")
#     if len(value) >= k:
#         print(f"value in if :{value}")
#         print(f"k in if : {k}")
#         # tmp = list(value)
#         answer = value[k-1]
#         print(answer)
#         exit(0)
#         return
#     # 문자열 0->1 1->0 바꾸고 value에 추가해주기
#     # tmp = []
#     for i in range(len(value)):
#         if value[i] == 0:
#             value.append(1)
#         else:
#             value.append(0)
#     ex(value)


# # result = ex([0])
# # value =
# ex([0])
# # print(replace("01"))

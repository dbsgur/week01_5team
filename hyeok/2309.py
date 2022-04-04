# import sys
# import itertools

# input = sys.stdin.readline


# talls = [int(input()) for _ in range(9)]

# talls.sort()

# result = list(itertools.combinations(talls, 7))

# for num in result:
#     nums = sum(num)
#     if nums == 100:
#         for n in num:
#             print(n)
#         break


# result = talls[i:i+7]

# print(result)

# another method - complete search

# import sys

# input = sys.stdin.readline

# talls = [int(input()) for _ in range(9)]

# talls.sort()

# x = sum(talls) - 100

# result = False

# for i in range(9):
#     for j in range(9):
#         if i == j:
#             continue
#         if (talls[i]+talls[j]) == x:
#             del talls[i]
#             del talls[j-1]
#             for tall in talls:
#                 print(tall)
#             sys.exit(0)
#             # result = True
#             # break
#     # if result == True:
#     #     break


# # for tall in talls:
# #     print(tall)


import sys

input = sys.stdin.readline

talls = [int(input()) for _ in range(9)]

talls.sort()

x = sum(talls) - 100

left = 0
right = 8
while left < right:
    confirm = talls[left] + talls[right]
    if confirm < x:
        left += 1
    elif confirm > x:
        right -= 1
    else:
        del talls[right]
        del talls[left]
        # print(talls)
        for tall in talls:
            print(tall)
        sys.exit(0)

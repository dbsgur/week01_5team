import sys

input = sys.stdin.readline

testScore = int(input())

if testScore >= 90:
    print("A")
elif testScore >= 80:
    print("B")
elif testScore >= 70:
    print("C")
elif testScore >= 60:
    print("D")
else:
    print("F")

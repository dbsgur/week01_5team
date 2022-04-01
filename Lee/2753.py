a= int(input())

if 0 == a%4 and 0 != a%100: #배수인지 알아볼땐 나머지가 0인지를 확인
    print('1')
elif 0 == a%400:
    print('1')
else:
    print('0')
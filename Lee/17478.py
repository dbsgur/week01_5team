import sys

input=sys.stdin.readline

n=int(input())

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

def reply(i,n):
    print('____'*i+'"재귀함수가 뭔가요?"')
    if i == n:
        print('____'*i+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print('____'*i+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____'*i+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____'*i+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        reply(i+1,n) #돌 때 마다 i값이 늘어나서 i==n이 되어 종료되게
    print('____'*i+'라고 답변하였지.')

reply(0,n) #내가 앞에 print 붙였던 것 삭제

#none 출력되었던건 해당 함수의 리턴값을 정해놓지 않앗기 때문에
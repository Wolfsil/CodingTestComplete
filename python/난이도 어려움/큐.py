import sys
from collections import deque


def solution(n):
    q=deque(maxlen= 2000001)
    for i in range(n):
        order=sys.stdin.readline().rstrip()
        if order[1]=="u":
            order=int(order.split()[1])
            q.append(order)
        elif order=="pop":
            if len(q)==0:
                print(-1)
            else:
                print(q.popleft())
        elif order=="size":
            print(len(q))
        elif order=="empty":
            if len(q)==0:
                print(1)
            else:
                print(0)
        elif order=="front":
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
        elif order=="back":
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])
                
if __name__=="__main__":
    n=int(sys.stdin.readline())     
    solution(n)

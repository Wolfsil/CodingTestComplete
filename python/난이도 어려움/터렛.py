import sys
     
def solotion(circle):
    for i in circle:
        x1,y1,r1,x2,y2,r2=i
        
        distance=((x1-x2)**2+(y1-y2)**2)**(0.5)
        maxDistence=r1+r2
        minDistence=abs(r1-r2)
      
            #완전히 겹치면 무한하겠다
        if (x1== x2 and y1==y2 and r1==r2):
            print(-1)
            #한점에 접할려면 최대길이가 같거나, 두 점사이의 거리가 반지름끼지의 차와 같을때(작은쪽이 빠지니까)
        elif distance==maxDistence or distance==minDistence:
            print(1)
            #반지름 차<거리<반지름 합
        elif distance<maxDistence and distance>minDistence:
            print(2)
        else:
            print(0)
        
if __name__=="__main__":
    n =int(sys.stdin.readline())
    circle=[]
    for i in range(n):
        circle.append(map(int,sys.stdin.readline().rstrip().split()))
    solotion(circle)


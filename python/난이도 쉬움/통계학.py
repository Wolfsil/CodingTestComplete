from itertools import count
import sys 


def solution(n,input):
    
    first=0
    second=0
    third=0
    forth=0
    thirdArr={}

    input=sorted(input)
    #1번, 3번
    for i in input:
        first+=i
        if i in thirdArr:
            thirdArr[i]= thirdArr[i]+1
        else:
            thirdArr[i]=1
    
    first= round((first/n))

    #2번
    if n%2==1:
        second=input[n//2]
    else:
        second=input[n//2]+input[n//2-1]

    #3번
    items=sorted(thirdArr.items(), key=lambda x:x[1], reverse=True)
    count=items[0][1]
    sameSize=[]
    for i in items:
        if i[1] == count:
            sameSize.append(i[0])
        else:
            break;
    sameSize.sort()
    third=sameSize[0]
    if len(sameSize)>1:
        third=sameSize[1]
    
    #4번
    forth = input[n-1]-input[0]

    print(first)
    print(second)
    print(third)
    print(forth)
            
if __name__=="__main__":
    n=int(sys.stdin.readline().rstrip())
    input=[]
    for i in range(n):
        input.append(int(sys.stdin.readline().rstrip()))
    solution(n,input)